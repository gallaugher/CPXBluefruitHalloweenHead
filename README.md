# CPXBluefruitHalloweenHead
NOTE: I should have clarified when I first posted this. LadyAda & Jeff Epler fixed an issue that caused a crash on the 4th sound play. The fix is in a.uf2 that isn't officially released, but Lady Ada kindly linked it in the follow up reply you can find here: adafruit/circuitpython#2203. If you can download a .uf2 for circuitpython that's greater than alpha 4 then you likely won't have the crash problem, otherwise refer to the .zip provided by ladyada in the link at adafruit/circuitpython#2203. Everything works fine if you use an updated .uf2.

Make a CPXb respond to touch + play sounds from the Bluefruit app

Uses an Adafruit Circuit Playground Express Bluefruit (CPXb)
https://www.adafruit.com/product/4333

And the Adafruit Bluefruit App
https://learn.adafruit.com/bluefruit-le-connect

Video demo at: http://bit.ly/cpxb-halloween-head-video


- Connect to the CPXb using the app
- Control Pad buttons 1-4 + Up play a sound file
- Touching CPXb pad A1 will scream
In the video I attached the CPXb's A1 pad to an alligator clip, then attached the other end of the clip to a copper wire cut into the top of a $10 skull mask I picked up at a Halloween shop.
- I also added an Adafruit MonsterM4sk - software is included in the purchase, so no additional code required for the mask.
https://www.adafruit.com/product/4343
- I also connected the CPXb to the inexpensive Adafruit STEMMA speaker:
https://www.adafruit.com/product/3885

cap touch on A1 will scream "Don't take candy from strangers!". Bluefruit App control pad #1 - #4 + Up Arrow light up CPXb and play a sound summoning the potential candy-taker.
Must include files:
"hey.wav"
"hey_you.wav"
"take_candy.wav"
"theres_candy_in_my_head.wav"
"open_my_head.wav"
   and
"ah_dont_take_candy_from_strangers.wav"
