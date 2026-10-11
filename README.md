# Baseball Stadium Trade Calculator

## Project Overview
This project solves a big problem in baseball stats: **stadium bias**. In Major League Baseball, fields aren't all the same size. Air density and altitude matter too. For example, hitting a home run at Coors Field (high altitude) is much easier than hitting one at T-Mobile Park (deep fences and heavy air). 

I wrote a Python script that takes a player's home runs from one stadium, clears out the stadium bias, and predicts how many home runs they would hit if they got traded to any of the other 30 MLB teams.

## How the Math Works
The script divides stadiums into 4 different tiers based on real-world MLB Park Factors (where 100 is perfectly average):
* **High Altitude Boost (Colorado):** 112
* **Hitter-Friendly Parks (Yankees, Boston, etc.):** 105
* **Neutral Parks (Dodgers, Cubs, etc.):** 100
* **Pitcher-Friendly Parks (Seattle, Giants, etc.):** 93

### The Equations:
1. **Find "Neutral" Home Runs:** `Neutral HR = Home Runs / (Current Park Factor / 100)`
2. **Predict New Home Runs:** `Projected HR = Neutral HR * (New Park Factor / 100)`

## How to Run It
1. Copy the code from the `main.py` file.
2. Go to an online interpreter like [online-python.com](https://online-python.com).
3. Paste the code into the editor and hit **Run**.
4. Type in your player's name, their home runs, and choose their stadiums using the numbers on the screen.

## Ideas for Future Updates
* Adding a weather feature that changes the math based on how hot or humid the field is on game day.
* Changing the code so it can track pitchers instead of hitters (like adjusting an ERA stat).
