# -*- coding: utf-8 -*-
"""NaiveBayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3kNVkacjKlULH7VfC4PKcagxUfncacG
"""

from google.colab import drive
drive.mount('/content/drive' ,force_remount=True)

import pandas as pd
from google.colab import files


uploaded = files.upload()


file_name = next(iter(uploaded))


try:
    data = pd.read_csv(file_name)
except Exception as e:
    print(f"Error reading the CSV file: {str(e)}")
    data = None

if data is not None:

    sunny_yes = hot_yes = overcast_yes = mild_yes = rain_yes = cool_yes = high_yes = normal_yes = weak_yes = strong_yes = 0
    sunny_no = hot_no = overcast_no = mild_no = rain_no = cool_no = high_no = normal_no = weak_no = strong_no = 0
    play_tennis_count_yes = play_tennis_count_no = total_rows = 0


    for index, row in data.iterrows():
        play_tennis = row['Play Tennis']
        total_rows += 1
        if play_tennis == 'Yes':
            play_tennis_count_yes += 1
        elif play_tennis == 'No':
            play_tennis_count_no += 1

        outlook = row['Outlook']
        temperature = row['Temperature']
        humidity = row['Humidity']
        wind = row['Wind']

        if play_tennis == 'Yes':
            if outlook == 'Sunny':
                sunny_yes += 1
            elif outlook == 'Overcast':
                overcast_yes += 1
            elif outlook == 'Rain':
                rain_yes += 1

            if temperature == 'Hot':
                hot_yes += 1
            elif temperature == 'Mild':
                mild_yes += 1
            elif temperature == 'Cool':
                cool_yes += 1

            if humidity == 'High':
                high_yes += 1
            elif humidity == 'Normal':
                normal_yes += 1

            if wind == 'Weak':
                weak_yes += 1
            elif wind == 'Strong':
                strong_yes += 1
        elif play_tennis == 'No':
            if outlook == 'Sunny':
                sunny_no += 1
            elif outlook == 'Overcast':
                overcast_no += 1
            elif outlook == 'Rain':
                rain_no += 1

            if temperature == 'Hot':
                hot_no += 1
            elif temperature == 'Mild':
                mild_no += 1
            elif temperature == 'Cool':
                cool_no += 1

            if humidity == 'High':
                high_no += 1
            elif humidity == 'Normal':
                normal_no += 1

            if wind == 'Weak':
                weak_no += 1
            elif wind == 'Strong':
                strong_no += 1


    print("Frequency of values when 'Play Tennis' = 'Yes':")
    print("Sunny_Yes:", sunny_yes)
    print("Hot_Yes:", hot_yes)
    print("Overcast_Yes:", overcast_yes)
    print("Mild_Yes:", mild_yes)
    print("Rain_Yes:", rain_yes)
    print("Cool_Yes:", cool_yes)
    print("High_Yes:", high_yes)
    print("Normal_Yes:", normal_yes)
    print("Weak_Yes:", weak_yes)
    print("Strong_Yes:", strong_yes)


    print("\nFrequency of values when 'Play Tennis' = 'No':")
    print("Sunny_No:", sunny_no)
    print("Hot_No:", hot_no)
    print("Overcast_No:", overcast_no)
    print("Mild_No:", mild_no)
    print("Rain_No:", rain_no)
    print("Cool_No:", cool_no)
    print("High_No:", high_no)
    print("Normal_No:", normal_no)
    print("Weak_No:", weak_no)
    print("Strong_No:", strong_no)


    print("\nOverall Frequencies:")
    print("Yes:", play_tennis_count_yes)
    print("No:", play_tennis_count_no)

freq_sunny_y = sunny_yes/play_tennis_count_yes
freq_cool_y  = cool_yes/play_tennis_count_yes
freq_high_y  = high_yes/play_tennis_count_yes
freq_strong_y= strong_yes/play_tennis_count_yes

freq_sunny_n = sunny_no/play_tennis_count_no
freq_cool_n  = cool_no/play_tennis_count_no
freq_high_n  = high_no/play_tennis_count_no
freq_strong_n= strong_no/play_tennis_count_no

ans_yes = (play_tennis_count_yes/14) * freq_strong_y * freq_high_y * freq_cool_y * freq_sunny_y
print("Yes ans is:",ans_yes)

ans_no = (play_tennis_count_no/14) * freq_strong_n * freq_high_n * freq_cool_n * freq_sunny_n
print("No ans is:",ans_no)

if(ans_yes>ans_no):
  print("He will play tennis")
else:
  print("He will not play tennis")