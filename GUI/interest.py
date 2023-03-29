import tkinter as tk
import textwrap
from functools import partial
from tkinter import *
# from database_controller import show_info, insert_baiscs


def Interest_Screen():
    root = tk.Tk()
    root.title("Basics Information")

    root.geometry('1280x800')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="GUI/sign_up_img/interest_img/background.png")

    continue_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/continue.png")

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )
    second_frame = Frame(my_canvas, width = 1280, height = 1921)
    label_background = tk.Label(second_frame, image = background)
    label_background.pack()
    my_canvas.create_window((0, 0), window= second_frame, anchor="nw")

    #----------------------------------------------------------------------------------------------------------------------------    
    #Interest 

    #Sport
    gym_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/gym.png")
    badminton_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/badminton.png")
    boxing_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/boxing.png")
    basketball_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/basketball.png")

    #Creativity
    design_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/design.png")
    photograph_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/photography.png")
    art_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/art.png")
    make_up_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/make-up.png")

    #Going out
    bars_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/bars.png")
    concerts_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/concerts.png")
    museums_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/museums.png") 
    cafe_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/cake.png")

    #Stayng in
    baking_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/baking.png") 
    cooking_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/cooking.png")
    board_game_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/board_game.png") 
    gardening_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/gardening.png")





    # Button no Click of Sport -- Creativity --  Going out -- Stayng in
    #Sport
    gym = tk.Button(second_frame, image=gym_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    gym.place(x = 130, y = 250)
    badminton = tk.Button(second_frame, image=badminton_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    badminton.place(x = 355, y = 250)
    boxing = tk.Button(second_frame, image=boxing_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    boxing.place(x = 130, y = 335)
    basketball = tk.Button(second_frame, image=basketball_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    basketball.place(x = 355, y = 335)

    #Creativity
    design = tk.Button(second_frame, image=design_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    photograph = tk.Button(second_frame, image=photograph_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    art = tk.Button(second_frame, image=art_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    make_up = tk.Button(second_frame, image=make_up_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Going out
    bars = tk.Button(second_frame, image=bars_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    concerts = tk.Button(second_frame, image=concerts_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    museums = tk.Button(second_frame, image=museums_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cafe = tk.Button(second_frame, image=cafe_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Stayng in
    baking = tk.Button(second_frame, image=baking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cooking = tk.Button(second_frame, image=cooking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    board_game = tk.Button(second_frame, image=board_game_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    gardening = tk.Button(second_frame, image=gardening_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)






    #----------------------------------------------------------------------------------------------------------------------------

    #Traveling
    backpacking_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/backpacking.png") 
    beaches_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/beaches.png") 
    winter_sports_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/winter_sports.png") 
    camping_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/camping.png")

    #Food & Drink
    sushi_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/sushi.png")
    pizza_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/pizza.png") 
    sweet_tooth_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/sweet_tooth.png")
    tea_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/tea.png")
    
    #Music
    classical_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/classical.png") 
    r_b_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/R&B.png")
    edm_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/edm.png")
    rap_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/music_img/rap.png")

    #Flim & TV
    action_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/action.png")
    romance_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/romance.png")
    comedy_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/comedy.png")
    horror_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/horror.png")
    #----------------------------------------------------------------------------------------------------------------------------
    # Button no Click of Traveling -- Food & Drink --  Music -- Flim & TV

    #Traveling
    backpacking = tk.Button(second_frame, image=backpacking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    beaches = tk.Button(second_frame, image=beaches_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    winter_sports = tk.Button(second_frame, image=winter_sports_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    camping = tk.Button(second_frame, image=camping_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Food & Drink
    sushi = tk.Button(second_frame, image=sushi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    pizza = tk.Button(second_frame, image=pizza_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    sweet_tooth = tk.Button(second_frame, image=sweet_tooth_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    tea = tk.Button(second_frame, image=tea_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    
    #Music
    classical = tk.Button(second_frame, image=classical_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    r_b = tk.Button(second_frame, image=r_b_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    edm = tk.Button(second_frame, image=edm_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    rap = tk.Button(second_frame, image=rap_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Flim & TV
    action = tk.Button(second_frame, image=action_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    romance = tk.Button(second_frame, image=romance_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    comedy = tk.Button(second_frame, image=comedy_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    horror = tk.Button(second_frame, image=horror_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)


    #----------------------------------------------------------------------------------------------------------------------------

    #Reading
    history_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/history.png")
    novel_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/novel.png")
    poetry_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/poetry.png")
    pschology_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/pschology.png")

    #Pets
    dog_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/dog.png")
    cat_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/cat.png")
    snake_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/snake.png")
    bird_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/bird.png")



    # Button no Click of Reading and Pets
    history = tk.Button(second_frame, image=history_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    novel = tk.Button(second_frame, image=novel_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    poetry = tk.Button(second_frame, image=poetry_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    pschology = tk.Button(second_frame, image=pschology_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Pets
    dog = tk.Button(second_frame, image=dog_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cat = tk.Button(second_frame, image=cat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    snake = tk.Button(second_frame, image=snake_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    bird = tk.Button(second_frame, image=bird_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    #----------------------------------------------------------------------------------------------------------------------------





    #----------------------------------------------------------------------------------------------------------------------------

    #Interest CLICK

    #Sport CLICK
    gym_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/gym.png")
    badminton_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/badminton.png")
    boxing_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/boxing.png")
    basketball_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/sport_img/basketball.png")

    #Creativity CLICK
    design_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/design.png")
    photograph_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/photograph.png")
    art_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/art.png")
    make_up_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/creativity_img/make_up.png")

    #Going out CLICK
    bars_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/bars.png")
    concerts_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/concerts.png")
    museums_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/museums.png") 
    cafe_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/going_out_img/cafe.png")

    #Stayng in CLICK
    baking_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/baking.png") 
    cooking_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/cooking.png")
    board_game_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/board_game.png") 
    gardening_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/gardening.png")

    #----------------------------------------------------------------------------------------------------------------------------

    # Button Click of Sport -- Creativity --  Going out -- Stayng in
    #Sport CLICK
    gym_click = tk.Button(second_frame, image=gym_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    #gym_click.place(x=171,y=475)
    badminton_click = tk.Button(second_frame, image=badminton_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    boxing_click = tk.Button(second_frame, image=boxing_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    basketball_click = tk.Button(second_frame, image=basketball_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Creativity CLICK
    design_click = tk.Button(second_frame, image=design_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    photograph_click = tk.Button(second_frame, image=photograph_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    art_click = tk.Button(second_frame, image=art_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    make_up_click = tk.Button(second_frame, image=make_up_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Going out CLICK
    bars_click = tk.Button(second_frame, image=bars_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    concerts_click = tk.Button(second_frame, image=concerts_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    museums_click = tk.Button(second_frame, image=museums_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cafe_click = tk.Button(second_frame, image=cafe_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Stayng in CLICK
    baking_click = tk.Button(second_frame, image=baking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cooking_click = tk.Button(second_frame, image=cooking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    board_game_click = tk.Button(second_frame, image=board_game_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    gardening_click = tk.Button(second_frame, image=gardening_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)





    #----------------------------------------------------------------------------------------------------------------------------

    #Traveling CLICK
    backpacking_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/backpacking.png") 
    beaches_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/beaches.png") 
    winter_sports_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/winter_sports.png") 
    camping_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/traveling_img/camping.png")


    #Food & Drink CLICK
    sushi_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/sushi.png")
    pizza_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/pizza.png") 
    sweet_tooth_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/sweet_tooth.png")
    tea_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/tea.png")
    

    #Music CLICK
    classical_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/classical.png") 
    r_b_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/R&B.png")
    edm_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/edm.png")
    rap_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/music_img/rap.png")

    #Flim & TV CLICK
    action_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/action.png")
    romance_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/romance.png")
    comedy_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/comedy.png")
    horror_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/horror.png")
    #----------------------------------------------------------------------------------------------------------------------------
    # Button Click of Traveling -- Food & Drink --  Music -- Flim & TV

    #Traveling CLICK
    backpacking_click = tk.Button(second_frame, image=backpacking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    beaches_click = tk.Button(second_frame, image=beaches_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    winter_sports_click = tk.Button(second_frame, image=winter_sports_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    camping_click = tk.Button(second_frame, image=camping_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Food & Drink CLICK
    sushi_click = tk.Button(second_frame, image=sushi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    pizza_click = tk.Button(second_frame, image=pizza_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    sweet_tooth_click = tk.Button(second_frame, image=sweet_tooth_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    tea_click = tk.Button(second_frame, image=tea_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    
    #Music CLICK
    classical_click = tk.Button(second_frame, image=classical_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0) 
    r_b_click = tk.Button(second_frame, image=r_b_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    edm_click = tk.Button(second_frame, image=edm_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    rap_click = tk.Button(second_frame, image=rap_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Flim & TV CLICK
    action_click = tk.Button(second_frame, image=action_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    romance_click = tk.Button(second_frame, image=romance_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    comedy_click = tk.Button(second_frame, image=comedy_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    horror_click = tk.Button(second_frame, image=horror_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)




    #----------------------------------------------------------------------------------------------------------------------------

    #Reading CLICK
    history_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/history.png")
    novel_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/novel.png")
    poetry_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/poetry.png")
    pschology_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/reading_img/psychology.png")

    #Pets CLICK
    dog_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/dog.png")
    cat_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/cat.png")
    snake_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/snake.png")
    bird_click_img = tk.PhotoImage(file="GUI/sign_up_img/interest_img/interest_click_img/pets_img/bird.png")


    # Button no Click of Reading and Pets
    history_click = tk.Button(second_frame, image=history_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    novel_click = tk.Button(second_frame, image=novel_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    poetry_click = tk.Button(second_frame, image=poetry_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    pschology_click = tk.Button(second_frame, image=pschology_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)

    #Pets
    dog_click = tk.Button(second_frame, image=dog_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cat_click = tk.Button(second_frame, image=cat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    snake_click = tk.Button(second_frame, image=snake_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    bird_click = tk.Button(second_frame, image=bird_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    #----------------------------------------------------------------------------------------------------------------------------


















    #----------------------------------------------------------------------------------------------------------------------------
    #Continue Button
    
    # continue_clickk = partial(continue_click, height, weight, zodiac, workout, smoke, drink, education, second_frame)
    
    continue_button = tk.Button(second_frame, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    continue_button.place(x = 200, y = 1800)
    root.mainloop()

if __name__ == "__main__":
    Interest_Screen()

