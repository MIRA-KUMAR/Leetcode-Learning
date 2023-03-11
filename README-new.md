# One Car, Two Car, Fast Car, Slow Car

**Details**
There are 3 different cars: _FastCar_, _SlowCar_, and _FancyCar_, derived from _AverageCar_. Each three has different functionalities and features w.r.t *SPEED*, *BRAKE EFFICIENCY*, *ACCELERATION*, *GEAR*. 

They travel on the Infinitely Long Road (ILR), a straight road with no wind resistance that goes on forever in both directions.
All cars have the stats of an average car unless otherwise stated.

Multiple cars can be driving at the same time, each on their own ILR. 

## Average Car

### Average Car stats

- Max Speed: 50 meters/sec
  - Any acceleration cannot make the car go faster than its max
- Acceleration: 5 meters/sec^2
  - If the car is accelerating forward, it is this value. Gas pedal acts as a binary switch
- Brake efficiency: -10 meters/sec^2
  - If the car is braking, it is this value. Brake pedal acts as a binary switch

### Average Car Features

1. turn on
   - turns on engine (allows for gas, driving, and braking to take affect)
   - establishing starting point ('home') on the ILR
2. turn off
   - turns off engine (disallows gas, driving, and braking)
   - engine cannot turn off while car is still moving (speed must be 0)
3. gas
   - adds gas to the engine, accelerates the car
   - Accelerates the car depending on how long the gas pedal is pressed (in secs)
   - Should accept a time value for how long the pedal is pressed to accelerate
   - should not affect distance, only affects speed
4. drive
   - continues driving in same direction
   - should accept a time value for how long to continue driving (in secs)
   - no change in acceleration (These cars should assume there is no natural deceleration, if the car is driving, then it is coasting at a steady speed)
   - average cars can only move forward
5. brake
   - slows down the vehicle
   - Should accept a time value for how long the pedal is pressed to brake (in secs)
   - should not affect distance, only affects speed
6. headlights
   - can turn on or off despite if the engine is on/off
7. check dashboard
   - should show current car stats:
     - engine on/off
     - headlights on/off
     - current speed
     - odometer:
       - distance traveled in trip
     - home:
       - distance from 'home'
     - current gear (direction car is moving)
       - park: when speed is 0
       - drive: moving forward
       - reverse: moving backward

---

## Unique Car Features

All of these features are the modifiers each unique car has compared to the average car stats

| Feature          | FastCar | SlowCar | FancyCar |
| ---------------- | :-----: | :-----: | :------: |
| Max Speed        |   3x    |  .75x   |    2x    |
| Acceleration     |   2x    |  .75x   |    1x    |
| Brake Efficiency |   1x    |   2x    |    1x    |

---

### FancyCar

1. drive/reverse gear change
   - changes the direction of the car [`drive` or `reverse`]. Total distance is additive no matter the direction; relative distance to 'home' will change depending on direction
   - cars can only change gears if speed is 0
   - speed of a car going in reverse is still tracked as positive
2. horn
   - Has a horn that goes "beep beep"

---

## Problem Statement

In the `main` race between them, here is what happens.

1. All three cars start their engines
2. `FastCar` and `FancyCar` turn on their lights
3. All three cars gas for 11 seconds
4. All three cars drive for 30 seconds
5. `FancyCar` brakes for 5 seconds, slowing down in order to enjoy the scenery around it, then continues driving for 3 seconds
6. `SlowCar` brakes for 6 seconds, curious what `FancyCar` is looking at
7. `FancyCar` realizes they left their lucky keychain behind and immediately brakes to a full stop, changes to reverse, gases for 20 seconds, then drives for an additional 30 seconds
8. `SlowCar` feels lonely (now that both cars have left it behind), comes to a full stop, then turns off its engine
9. After realizing headlights aren't that useful while going in reverse, `FancyCar` turns off its lights
10. `FastCar`, all the while, continues driving for another 30 seconds, gasses 20 seconds, and drives an addition 60 seconds
11. All three cars check their dashboards
12. `FancyCar` honks its horn twice, celebrating that it found its lost keychain
13. `SlowCar`, starts to get cold in the infinite nothingness. It turns on its engine again, turns on its lights, gases for 4 seconds, and then drives for 2000 seconds into the inifinite beyond
14. `SlowCar` checks its dashboard

---

## Requirements
1. Python v3
2. Pip v3

---

## Process 

**Tested on MacOS (Apple M1)(Version 11.5.1) and Windows 10 (Intel i5)**

1. Change directory to project by using
```bash
cd cars/
```

---

2. Install required packages by using command
```bash
pip3 install -r requirements.txt
```

      To upgrade pip, execute;
      `python.exe -m pip install --upgrade pip`

---

3. To run **Problem Statement** execute;

    `python3 main.py` || `python main.py`

---

3. To run tests execute;

    ```bash
    cd tests\
    ```
    ```bash
    pytest
    ```

---

## File Structure

cars/
|-- test/
|   |-- test_main.py
|   |-- test_fast_car.py
|   |-- test_slow_car.py
|   |-- test_avg_car.py
|   |-- test_fancy_car.py
|  
|-- README.md
|-- main.py
|-- base_car.py


---
