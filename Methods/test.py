full_name_list = [('Joe', 'Schmoe', 23),
                  ('Earnst', 'Ehlmann', 65),
                  ('Thomas', 'Fischer', 11),
                  ('Martin', 'Walter', 36),
                  ('Charles', 'Rogan', 83)]

first_name, last_name, age = list(zip(*full_name_list))
print(f"first name: {first_name}\nlast name: {last_name} \nage: {age}")