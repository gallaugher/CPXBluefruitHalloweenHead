# CPXBluefruitHalloweenHead
Make a Circuit Playground Bluefruit respond to touch + play sounds from the Bluefruit app

Uses an Adafruit Circuit Playground Bluefruit (CBP)
https://www.adafruit.com/product/4333

And the Adafruit Bluefruit App
https://learn.adafruit.com/bluefruit-le-connect

Video demo at: http://bit.ly/cpxb-halloween-head-video

- Connect to the CPB using the app
- Control Pad buttons 1-4 + Up play a sound file
- Touching CPB pad A1 will scream
In the video I attached the CPB's A1 pad to an alligator clip, then attached the other end of the clip to a copper wire cut into the top of a $10 skull mask I picked up at a Halloween shop.
- I also added an Adafruit MonsterM4sk - software is included in the purchase, so no additional code required for the mask.
https://www.adafruit.com/product/4343
- I also connected the CPXb to the inexpensive Adafruit STEMMA speaker:
https://www.adafruit.com/product/3885

cap touch on A1 will scream "Don't take candy from strangers!". Bluefruit App control pad #1 - #4 + Up Arrow light up CPB and play a sound summoning the potential candy-taker.
Must include files in a folder named "sound" on the CPB:
"hey.wav"
"hey_you.wav"
"take_candy.wav"
"theres_candy_in_my_head.wav"
"open_my_head.wav"
   and
"ah_dont_take_candy_from_strangers.wav"
