#!/bin/bash
# Screenshot lesson screens from build/NN.html (run build.py --only NN first).
# usage: course/shoot.sh NN i [i ...]        i = screen number, 0 for Start, done for Done
#        THEME=light course/shoot.sh NN i    light mode instead of dark
#        PHONE_H=2400 course/shoot.sh NN i   a taller phone shot, to see the bottom of long screens
# writes course/shots/NN-i-desktop.png (1440x900) and course/shots/NN-i-phone.png (390 wide)
set -e
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/shots"
lesson=$1; shift
theme=${THEME:-dark}
phone_h=${PHONE_H:-844}
# a throwaway profile per run, so several lessons can screenshot at once
prof=$(mktemp -d)
trap 'rm -rf "$prof"' EXIT
page="$DIR/shots/page-$lesson-$theme.html"
{
  printf '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>'
  printf '<script>document.documentElement.dataset.theme="%s";try{localStorage.clear()}catch(e){}</script>\n' "$theme"
  cat "$DIR/build/$lesson.html"
} > "$page"
for i in "$@"; do
  if [ "$i" = 0 ]; then h="lesson-$lesson"; elif [ "$i" = done ]; then h="lesson-$lesson-done"; else h="lesson-$lesson-$i"; fi
  tag="$lesson-$i"
  [ "$theme" = light ] && tag="$tag-light"
  "$CH" --headless=new --user-data-dir="$prof" --disable-gpu --hide-scrollbars --window-size=1440,900 --virtual-time-budget=3000 \
    --screenshot="$DIR/shots/$tag-desktop.png" "file://$page#$h" >/dev/null 2>&1
  # headless Chrome will not make a window narrower than 500px, so phones render in a 390px iframe
  printf '<!doctype html><body style="margin:0;background:#888"><iframe src="%s" width="390" height="%s" style="border:0"></iframe></body>' "file://$page#$h" "$phone_h" > "$DIR/shots/phone-$lesson.html"
  "$CH" --headless=new --user-data-dir="$prof" --disable-gpu --hide-scrollbars --window-size=500,$phone_h --virtual-time-budget=3000 \
    --screenshot="$DIR/shots/$tag-phone.png" "file://$DIR/shots/phone-$lesson.html" >/dev/null 2>&1
  echo "$DIR/shots/$tag-desktop.png $DIR/shots/$tag-phone.png"
done
