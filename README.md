# Test_task_for_Space_Lab_Team
Recommended Libraries: requests / Beautiful Soup 4

Task:

1. Using the bs4 library, parse the list of countries from the page https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3 %D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2.

2. Count the number of countries starting with the same letter. Count the number of words in the full name of the country. Get the url of the flag.

3. Write as a list of dicts:

EXAMPLE : 

 [{"country": "Австралия", 
"full_country_name": "Австралийский Союз",
"same_letter_count": 11,
"flag_url": "upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/50px-Flag_of_Australia.svg.png"},]

4. Create a function that will display a dictionary with the data of a specific country by its short name.