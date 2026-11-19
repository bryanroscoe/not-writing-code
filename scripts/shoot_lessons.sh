#!/bin/bash
# Screenshot lesson screens from build/lessons/NN.html (run scripts/build_lessons.py --only NN first).
# usage: scripts/shoot_lessons.sh NN i [i ...]        i = screen number, 0 for Start, done for Done
#        THEME=light scripts/shoot_lessons.sh NN i    light mode instead of dark
#        PHONE_H=2400 scripts/shoot_lessons.sh NN i   a taller phone shot, to see the bottom of long screens
# writes build/lessons/shots/NN-i-desktop.png (1440x900) and build/lessons/shots/NN-i-phone.png (390 wide)
set -e
CH="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
OUT="$(cd "$(dirname "$0")/.." && pwd)/build/lessons"
mkdir -p "$OUT/shots"
lesson=$1; shift
theme=${THEME:-dark}
phone_h=${PHONE_H:-844}
# a throwaway profile per run, so several lessons can screenshot at once
prof=$(mktemp -d)
trap 'rm -rf "$prof"' EXIT
page="$OUT/shots/page-$lesson-$theme.html"
sed "s#<head>#<head><script>document.documentElement.dataset.theme='$theme'</script>#" "$OUT/$lesson.html" > "$page"
for i in "$@"; do
  if [ "$i" = 0 ]; then h="lesson-$lesson"; elif [ "$i" = done ]; then h="lesson-$lesson-done"; else h="lesson-$lesson-$i"; fi
  tag="$lesson-$i"
  [ "$theme" = light ] && tag="$tag-light"
  "$CH" --headless=new --user-data-dir="$prof" --disable-gpu --hide-scrollbars --window-size=1440,900 --virtual-time-budget=3000 \
    --screenshot="$OUT/shots/$tag-desktop.png" "file://$page#$h" >/dev/null 2>&1
  # headless Chrome will not make a window narrower than 500px, so phones render in a 390px iframe
  printf '<!doctype html><body style="margin:0;background:#888"><iframe src="%s" width="390" height="%s" style="border:0"></iframe></body>' "file://$page#$h" "$phone_h" > "$OUT/shots/phone-$lesson.html"
  "$CH" --headless=new --user-data-dir="$prof" --disable-gpu --hide-scrollbars --window-size=500,$phone_h --virtual-time-budget=3000 \
    --screenshot="$OUT/shots/$tag-phone.png" "file://$OUT/shots/phone-$lesson.html" >/dev/null 2>&1
  echo "$OUT/shots/$tag-desktop.png $OUT/shots/$tag-phone.png"
done
