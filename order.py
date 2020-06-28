from selenium import webdriver
from random_word import RandomWords
from random import randrange

def get_user_details():
    username = input("enter your name: ")
    useremail = input("enter your email id: ")
    return [username, useremail]

def get_input():
    region = input("\nRegion:\n1. Prod\n2. Test\n")
    plan = input("\nPlan:\n1. Saver\n2. Normal\n3. Full\n")
    if (region in ("1", "2")) and (plan in ("1", "2", "3")):
        return [region, plan]
    else:
        return get_input()

def navigate_to_plan(input_data):
    region = input_data[0]
    plan = input_data[1]
    if region == '1':
        driver.get("https://www.wrapyourbook.com")
    elif region == '2':
        driver.get("http://127.0.0.1:8000")
    button = ""
    if plan == '1':
        button = driver.find_element_by_id("saver-button")
    elif plan == '2':
        button = driver.find_element_by_id('normal-button')
    elif plan == '3':
        button = driver.find_element_by_id('full-button')
    driver.execute_script("arguments[0].click();", button)

def fill_data(userinfo):
    name = driver.find_element_by_name("name")
    email = driver.find_element_by_name("email")
    title = driver.find_element_by_name("title")
    author = driver.find_element_by_name("author")
    genre = driver.find_element_by_name("genre")
    color = driver.find_element_by_name("color")
    keyword = driver.find_element_by_name("keyword")
    inspiration = driver.find_element_by_name("inspiration")
    remarks = driver.find_element_by_name("remarks")

    word = RandomWords()
    genre_array = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Tragedy']
    color_array = ['Red', 'Blue', 'Green', 'Yellow', 'Gray', 'Black', 'White']
    genre_number = randrange(0, len(genre_array)-1, 1)
    color_number = randrange(0, len(color_array)-1, 1)
    new_title = word.get_random_word()


    name.send_keys(userinfo[0])
    email.send_keys(userinfo[1])
    title.send_keys(new_title)
    author.send_keys(userinfo[0])
    genre.send_keys(genre_array[genre_number])
    color.send_keys(color_array[color_number]) 
    keyword.send_keys(word.get_random_word())
    inspiration.send_keys("wwww.wrapyourbook.com")
    remarks.send_keys(word.get_random_word())

    print("\nName of the book: " + new_title + "\n")
    print("Username: " + userinfo[0] + '\n')
    print("User Email: " + userinfo[1] + "\n")

def place_order():
    submit_button = driver.find_element_by_id("submit_button")
    driver.execute_script("arguments[0].click();", submit_button)


userinfo = get_user_details()
input_data = get_input()
driver = webdriver.Chrome()
navigate_to_plan(input_data)
fill_data(userinfo)
place_order()   