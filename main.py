import time
from turtle import Screen

from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_true = True
while game_is_true:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
       if car.distance(player) < 20:
           game_is_true = False

    # #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()



screen.exitonclick()
