from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pygame
import random
import time
#SOUNDS
pygame.init()
pygame.mixer.init()

button_sound = pygame.mixer.Sound("C:\Capstone\gaudios\sound_b1.mp3")

def singleplayermode():
    time_limit = 30
    start_time = time.time()
    correct_answers = 1
    elapsed_time = time_limit - int(time.time() - start_time)

    easy_words = ['cat', 'dog', 'sun', 'pen', 'hat', 'red', 'big', 'cup', 'run', 'top',
                  'bus', 'rain', 'book', 'fish', 'bird', 'ball', 'moon', 'tree', 'star', 'jump',
                  'hill', 'blue', 'lamp', 'bell', 'frog', 'duck', 'soft', 'loud', 'tiny', 'fast',
                  'cake', 'ring', 'sing', 'pink', 'flip', 'flag', 'dark', 'tall', 'ship', 'wind',
                  'fire', 'cold', 'play', 'swim', 'jump', 'bike', 'deep', 'kind', 'open', 'shut']

    medium_words = ['happy', 'apple', 'beach', 'green', 'black', 'juice', 'jelly', 'zebra', 'robot', 'table',
                    'giant', 'sunny', 'happy', 'sugar', 'globe', 'smile', 'water', 'music', 'chase', 'fancy',
                    'elect', 'bunny', 'piano', 'ocean', 'kitty', 'lucky', 'party', 'magic', 'candy', 'queen',
                    'crazy', 'trick', 'cloud', 'fruit', 'dizzy', 'spark', 'flame', 'swing', 'beard', 'braid',
                    'swirl', 'crane', 'sweep', 'greet', 'shade', 'toast', 'vivid', 'mango', 'sweep', 'swirl']

    hard_words = ['solution', 'triangle', 'language', 'elephant', 'colorful', 'children', 'magnetic', 'delicate',
                  'birthday', 'favorite',
                  'knowledge', 'discovery', 'hospital', 'beautiful', 'mysterious', 'adventure', 'celebrate',
                  'enthusiasm', 'chocolate', 'explosion',
                  'generation', 'harmony', 'magnifico', 'oblivious', 'quizzical', 'serenity', 'turbulent',
                  'waterfall', 'quintuple']

    scramble_label = Label(main_menu, text="")
    scramble_label.pack()

    Score = elapsed_time / correct_answers

    def preparation():
        for widget in main_menu.winfo_children():
            widget.destroy()
        ready = Label(main_menu, text="Press your intended DIFFiCULTY when you ready")
        ready.pack()

        easy_single = Button(main_menu, text="EASY", command=game_easy)
        easy_single.pack()

        medium_single = Button(main_menu, text="MEDIUM", command=game_medium)
        medium_single.pack()

        hard_single = Button(main_menu, text="HARD", command=game_hard)
        hard_single.pack()

        back_button = Button(main_menu, text="Back")
        back_button.pack()

    def game_easy():
        for widget in main_menu.winfo_children():
            widget.destroy()

        scramble_label = Label(main_menu, text="")
        scramble_label.pack()

        entry = Entry(main_menu)
        entry.pack()

        timer_label = Label(main_menu, text="")
        timer_label.pack()

        score_label = Label(main_menu, text=f"Score: {Score}")
        score_label.pack()

        Correct_label = Label(main_menu, text="Correct Guesses:0")
        Correct_label.pack()

        global correct_answers, start_time

        def update_timer():
            global correct_answers, final_score
            elapsed_time = time_limit - int(time.time() - start_time)
            if correct_answers < 10:
                if elapsed_time > 0:
                    timer_label.config(text=f"Time Left: {elapsed_time} seconds")
                    main_menu.after(1000, update_timer)

                else:
                    timer_label.config(text="Time's up!!")
                    entry.destroy()
                    scramble_label.destroy()



        def word_generator():
            global correct_answers
            if correct_answers < 10:
                chosen_word = random.choice(easy_words)
                easy_words.remove(chosen_word)
                letters = list(chosen_word)
                random.shuffle(letters)

                scrambled_word = "".join(letters)
                scramble_label.config(text="Scrambled word: " + scrambled_word)

                def answer_checker():
                    global correct_answers
                    if entry.get() == chosen_word:
                        correct_answers += 1
                        entry.delete(0, END)
                        word_generator()
                        Score = elapsed_time / correct_answers
                        score_label.config(text=f"Score: {Score}")
                        Correct_label.config(text=f"Correct Guesses: {correct_answers}")
                        submit_button.destroy()
                        back_button.destroy()

                    else:
                        wrong_answer = Label(main_menu, text="Wrong Answer")
                        wrong_answer.pack()

                        def destroy_wrong_answer():
                            wrong_answer.destroy()
                        main_menu.after(2000, destroy_wrong_answer)


                submit_button = Button(main_menu, text="SUBMIT", command=answer_checker)
                submit_button.pack()

                back_button = Button(main_menu, text="Back",command=preparation)
                back_button.pack()

                def on_enter_key(event):
                    answer_checker()

                main_menu.bind('<Return>', on_enter_key)
            else:
                scramble_label.config(text='Game Over!!')
                back_button = Button(main_menu, text="Back",command=preparation)
                back_button.pack()

        correct_answers = 0
        start_time = time.time()
        update_timer()
        word_generator()

    def game_medium():
        for widget in main_menu.winfo_children():
            widget.destroy()

        scramble_label = Label(main_menu, text="")
        scramble_label.pack()

        entry = Entry(main_menu)
        entry.pack()

        timer_label = Label(main_menu, text="")
        timer_label.pack()

        score_label = Label(main_menu, text=f"Score: {Score}")
        score_label.pack()

        Correct_label = Label(main_menu, text="Correct Guesses:0")
        Correct_label.pack()

        global correct_answers, start_time

        def update_timer():
            elapsed_time = time_limit - int(time.time() - start_time)
            if correct_answers < 10:
                if elapsed_time > 0:
                    timer_label.config(text=f"Time Left: {elapsed_time} seconds")
                    main_menu.after(1000, update_timer)
                else:
                    timer_label.config(text="Time's up!!")
                    entry.destroy()
            else:
                timer_label.config(text="Game Over!!")

        def word_generator():
            global correct_answers
            if correct_answers < 10:
                chosen_word = random.choice(medium_words)
                medium_words.remove(chosen_word)
                letters = list(chosen_word)
                random.shuffle(letters)

                scrambled_word = "".join(letters)
                scramble_label.config(text="Scrambled word: " + scrambled_word)

                def answer_checker():
                    global correct_answers
                    if entry.get() == chosen_word:
                        correct_answers += 1
                        entry.delete(0, END)
                        word_generator()
                        Score = elapsed_time / correct_answers
                        score_label.config(text=f"Score: {Score}")
                        Correct_label.config(text=f"Correct Guesses: {correct_answers}")
                        submit_button.destroy()
                        back_button.destroy()
                    else:
                        wrong_answer = Label(main_menu, text="Wrong Answer")
                        wrong_answer.pack()

                        def destroy_wrong_answer():
                            wrong_answer.destroy()

                        main_menu.after(2000, destroy_wrong_answer)

                submit_button = Button(main_menu, text="SUBMIT", command=answer_checker)
                submit_button.pack()

                back_button = Button(main_menu, text="Back",command=preparation)
                back_button.pack()
                def on_enter_key(event):
                    answer_checker()

                main_menu.bind('<Return>', on_enter_key)
            else:
                scramble_label.config(text='Game Over!!')
                back_button = Button(main_menu, text="Back",command=preparation)
                back_button.pack()

        correct_answers = 0
        start_time = time.time()
        update_timer()
        word_generator()

    def game_hard():
        for widget in main_menu.winfo_children():
            widget.destroy()

        scramble_label = Label(main_menu, text="")
        scramble_label.pack()

        entry = Entry(main_menu)
        entry.pack()

        timer_label = Label(main_menu, text="")
        timer_label.pack()

        score_label = Label(main_menu, text=f"Score: {Score}")
        score_label.pack()

        Correct_label = Label(main_menu, text="Correct Guesses:0")
        Correct_label.pack()

        global correct_answers, start_time

        def update_timer():
            elapsed_time = time_limit - int(time.time() - start_time)
            if correct_answers < 10:
                if elapsed_time > 0:
                    timer_label.config(text=f"Time Left: {elapsed_time} seconds")
                    main_menu.after(1000, update_timer)

                else:
                    timer_label.config(text="Time's up!!")
                    entry.destroy()
            else:
                timer_label.config(text="Game Over!!")

        def word_generator():
            global correct_answers
            if correct_answers < 10:
                chosen_word = random.choice(hard_words)
                hard_words.remove(chosen_word)
                letters = list(chosen_word)
                random.shuffle(letters)

                scrambled_word = "".join(letters)
                scramble_label.config(text="Scrambled word: " + scrambled_word)

                def answer_checker():
                    global correct_answers
                    if entry.get() == chosen_word:
                        correct_answers += 1
                        entry.delete(0, END)
                        word_generator()
                        Score = elapsed_time / correct_answers
                        main_menu.after(1000, score_label)
                        score_label.config(text=f"Score: {Score}")
                        Correct_label.config(text=f"Correct Guesses: {correct_answers}")
                        submit_button.destroy()
                        back_button.destroy()

                    else:
                        wrong_answer = Label(main_menu, text="Wrong Answer")
                        wrong_answer.pack()

                        def destroy_wrong_answer():
                            wrong_answer.destroy()
                        main_menu.after(2000, destroy_wrong_answer)

                submit_button = Button(main_menu, text="SUBMIT", command=answer_checker)
                submit_button.pack()

                back_button = Button(main_menu, text="Back",command=preparation)
                back_button.pack()
                def on_enter_key(event):
                    answer_checker()

                main_menu.bind('<Return>', on_enter_key)
            else:
                scramble_label.config(text='Game Over!!')
                back_button = Button(main_menu, text="Back", command=preparation)
                back_button.pack()

        correct_answers = 0
        start_time = time.time()
        update_timer()
        word_generator()
    preparation()

def play():
    pygame.mixer.music.load("C:\Capstone\gaudios\music_game.mp3")
    pygame.mixer_music.play(-1)
    pygame.mixer.music.set_volume(0.2)

def stop_music():
    pygame.mixer.music.stop()

def play_button_sound():
    button_sound.play()

#MAIN MENU
main_menu = Tk()
main_menu.title("WORD WARS")
main_menu.geometry("500x500")
main_menu_bg_1 = tk.PhotoImage(file="C:\Capstone\modules\home_page.png")
main_menu_bg_2 = tk.PhotoImage(file="C:\Capstone\modules\home_page.png")
credits_main_bg = tk.PhotoImage(file="C:\Capstone\modules\credits_ui.png")
main_menu.config(background="#183D3D")
background_1 = Label(main_menu, image=main_menu_bg_1)
background_1.pack()

#PAGE DESTROYER
def clear_page():
    for child in main_menu.winfo_children():
        child.destroy()

#CREDITS PAGE
def credits_page():
    clear_page()
    main_menu.geometry("500x500")
    background_2 = Label(main_menu, image=credits_main_bg)
    background_2.pack()

    credits_path = tk.PhotoImage(file="C:\Capstone\modules\credits.png")
    credits_label = tk.Label(main_menu, image=credits_path, borderwidth=0, width=400, height=400, relief="flat", background="#183D3D", activebackground="#183D3D")
    credits_label.place(x=50, y=50)

    b_main_menu_2_path = tk.PhotoImage(file="C:\Capstone\modules\mainmenubutton.png")
    main_menu_button_2 = tk.Button(main_menu, image=b_main_menu_2_path, borderwidth=0, width=145, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command=credits_b_main_menu)
    main_menu_button_2.place(x=180, y=400)

    main_menu.mainloop()

#OPTION PAGE
def option_page():
    clear_page()
    main_menu.geometry("500x500")
    background_1 = Label(main_menu, image=main_menu_bg_1)
    background_1.pack()

    no_music_path = tk.PhotoImage(file="C:\Capstone\modules\stop_music_button.png")
    no_music_button = tk.Button(main_menu, image=no_music_path, borderwidth=0, width=150, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= option_s_m)
    no_music_button.place(x=180, y=230)

    b_main_menu_3_path = tk.PhotoImage(file="C:\Capstone\modules\mainmenubutton.png")
    main_menu_button_3 = tk.Button(main_menu, image=b_main_menu_3_path, borderwidth=0, width=145, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= option_b_main_menu)
    main_menu_button_3.place(x=180, y=350)

    main_menu.mainloop()

#START PAGE
def start_page():
    clear_page()
    background_1 = Label(main_menu, image=main_menu_bg_1)
    background_1.pack()

    singleplayer_b_path = tk.PhotoImage(file="C:\Capstone\modules\singleplayerbutton.png")
    singleplayer_button = tk.Button(main_menu, image=singleplayer_b_path, borderwidth=0, width=145, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= singleplayer_page)
    singleplayer_button.place(x=180, y=170)

    multiplayer_b_path = tk.PhotoImage(file="C:\Capstone\modules\multiplayerbutton.png")
    multiplayer_button = tk.Button(main_menu, image=multiplayer_b_path, borderwidth=0, width=145, height=50, relief="flat", background="#183D3D", activebackground="#183D3D")
    multiplayer_button.place(x=180, y=230)

    time_attack_b_path = tk.PhotoImage(file="C:\Capstone\modules\ontimeattackbutton.png")
    time_attack_button = tk.Button(main_menu, image=time_attack_b_path, borderwidth=0, width=145, height=50, relief="flat", background="#183D3D", activebackground="#183D3D")
    time_attack_button.place(x=180, y=290)

    b_main_menu_1_path = tk.PhotoImage(file="C:\Capstone\modules\mainmenubutton.png")
    main_menu_button_1 = tk.Button(main_menu, image=b_main_menu_1_path, borderwidth=0, width=145, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= play_b_main_menu)
    main_menu_button_1.place(x=180, y=350)

    main_menu.mainloop()

#MAIN PAGE
def page_1():
    clear_page()
    main_menu.geometry("500x500")
    background_1 = Label(main_menu, image=main_menu_bg_1)
    background_1.pack()

    play_b_path = tk.PhotoImage(file= "C:\Capstone\modules\playbutton.png") 
    play_button = tk.Button(main_menu, image=play_b_path, borderwidth=0, width=80, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= enter_game_page)
    play_button.place(x=210, y=170)

    option_b_path = tk.PhotoImage(file="C:\Capstone\modules\optionsbutton.png")
    option_button = tk.Button(main_menu, image=option_b_path, borderwidth=0, width=100, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= enter_option_page)
    option_button.place(x=200, y=230)

    credits_b_path = tk.PhotoImage(file="C:\Capstone\modules\creditsbutton.png")
    credits_button = tk.Button(main_menu, image=credits_b_path, borderwidth=0, width=100, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= enter_credits_page)
    credits_button.place(x=200, y=290)

    exit_b_path = tk.PhotoImage(file="C:\Capstone\modules\exitbutton.png")
    exit_button = tk.Button(main_menu, image=exit_b_path, borderwidth=0, width=100, height=50, relief="flat", background="#183D3D", activebackground="#183D3D", command= exit_game)
    exit_button.place(x=200, y=350)

    main_menu.mainloop()

#COMMANDS
def enter_game_page():
    play_button_sound()
    start_page()

def enter_option_page():
    play_button_sound()
    option_page()

def enter_credits_page():
    play_button_sound()
    credits_page()

def exit_game():
    play_button_sound()
    main_menu.destroy()

def credits_b_main_menu():
    play_button_sound()
    page_1()

def option_b_main_menu():
    play_button_sound()
    page_1()

def play_b_main_menu():
    play_button_sound()
    page_1()

def option_s_m():
    play_button_sound()
    stop_music()

def singleplayer_page():
    play_button_sound()
    singleplayermode()

#RUN
play()
page_1()
main_menu.mainloop()