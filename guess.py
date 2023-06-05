import locklib as locker

print("\033[1;32m\t ### GUESS THE LOCKER ### \t")
print("\033[1;32m\t  @@ PRESS -1 FOR INFO @@")
print("\033[1;32m\t   @@ PRESS 1 TO PLAY @@")
print("\033[1;32m\t   @@ PRESS 0 TO EXIT @@\n")

option = int(input("\033[1;0mSelect your option: "))

play_value = locker.play(option)

while (play_value):
  option = int(input("\033[1;0mSelect your option: "))
  play_value = locker.play(option)