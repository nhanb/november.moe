Might as well.

# ~~Excuses~~Rationales

## Graceful degradation

Works fine with JavaScript disabled.  This is achieved by using native HTML5 /
CSS3 features whenever possible.  It also means no fancy multilingual support -
of course I could generate separate /en/ & /vi/ static versions but that then
means a level of indirection on the homepage; also all that work wouldn't Spark
Joy (tm).  As a consolation price, English translations are available in the
form of `title` attributes, which appear on mouseover, but obviously won't work
on mobile, which brings us to...

## Desktop-first

Though it should look presentable on mobile, I refuse to bend over backwards
for the Eternal September device.
