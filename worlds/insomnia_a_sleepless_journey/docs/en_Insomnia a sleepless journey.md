# Insomnia a sleepless journey

## I haven't played Insomnia before.
The game is pretty small, and I tried to make it as user-friendly as possible, and the game doesn't really have any spoilers, so even if you didn't play vanilla you should be able to play the randomizer.

## How is this game different from vanilla?
First, obviously, it includes archipelago client which allows randomization.  
I've also changed a few keybinds, because I felt the game would play better this way:  
You now don't need to hold Z ~~the entire game~~ to run.  
Jump is now Z instead of X.  
Attack is now X instead of C.  
Slide is now C instead of Down+Jump.  

I also removed switch mechanic for a few reasons:  
1. It was annoying. Imagine you explore some region just to find out that you needed to use a switch before.
2. It was hard to implement in rules.
3. It was buggy: a switch was inactive after you press it, and you had to use another switch. But in fact you could just restart the game, and switch would be active again. Abusing game restart is not fun.
4. It didn't add almost anything meaningful: you were able to reach switches only pretty late in game, when you don't really need them.
5. I'm sorry about this, Jani.  

I also changed how map works: before you would get map from chest outside starting house, very early. But with randomizer the map could be literally anywhere, so the player would have to run around with no map at all. Now you always have the map, and getting the "Magic map" item makes the map a bit better. I really hated that the map has no outlines, so adjacent rooms could not have a connection.  

Connections now show if you have "Brain" item, and require only one room to be visited, unlike 2 in vanilla.

I've also commited a few crimes in the code to make client work, but who cares.


## What does randomization do to this game?
All items you normally find in chests, all stars, all enemies, and fans switch are shuffled into the item pool.
Locations that contain random items from the item pool include opening chests, collecting stars, killing enemies, and using fans switch.

## What is the goal of Insomnia when randomized?
The goal is the same as the vanilla game. Get 99 stars and 99 kills (NOT kill 99 enemies, get 99 kills!), and enter the door at the top, then walk through ending location.

## How many checks are in Insomnia?
13 chests, 99 stars, 99 enemies, 1 switch.  
212 checks.

## What do items from other worlds look like in Insomnia?
You collect the item how it looks in Insomnia, and get message that your item was sent to another world.

## Is there a tracker?
There's a tracker for stars and kills count. Not for equipment or fans switch.

## What should I know regarding logic?
The game might require to do some insane tricks with lubricant, the best item in the game : )  
(If you slide, then after a few frames attack, you can instantly jump, giving you more height than slide+jump)

## Who contributed to this?
Only me, Dzhake.