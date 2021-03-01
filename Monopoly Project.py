'''
Monopoly Final
'''

#Steps
'''
-spaces, names, rents
-dice roll,moving around the board
-player totals
-visual(?)
-strategy/choices/inputs(?)
-game logic
'''
#Imports
import random
import sys

#Variables
board_spaces=["GO","Mediterranean Avenue","Community Chest","Baltic Avenue","Income Tax",
              "Reading Railroad","Oriental Avenue","Chance","Vermont Avenue","Connecticut Avenue",
              "Jail/Just Visiting","St. Charles Place","Electric Company","States Avenue","Virginia Avenue",
              "Pennsylvania Railroad","St. James Place","Community Chest","Tenessee Avenue","New York Avenue",
              "Free Parking","Kentucky Avenue","Chance","Indiana Avenue","Illinois Avenue",
              "B&O Railroad","Atlantic Avenue","Ventnor Avenue","Water Works","Marvin Gardens",
              "Go To Jail","Pacific Avenue","North Carolina Avenue","Community Chest","Pennsylvania Avenue",
              "Short Line","Chance","Park Place","Luxury Tax","Boardwalk"]


rent_list=[0,(2,10,30,90,160,250),0,(4,20,60,180,320,450),0,
      (25,50,100,200),(6,30,90,270,400,550),0,(6,30,90,270,400,550),(8,40,100,300,450,600),
       0,(10,50,150,450,625,750),(4,10),(10,50,150,450,625,750),(12,60,180,500,700,900),
      (25,50,100,200),(14,70,200,550,750,950),0,(14,70,200,550,750,950),(16,80,220,600,800,1000),
       0,(18,90,250,700,875,1050),0,(18,90,250,700,875,1050),(20,100,300,750,925,1100),
      (25,50,100,200),(22,110,330,800,975,1150),(22,110,330,800,975,1150),(4,10),(24,120,360,850,1025,1200),
       0,(26,130,390,900,1100,1275),(26,130,390,900,1100,1275),0,(28,150,450,1000,1200,1400),
      (25,50,100,200),0,(35,175,500,1100,1300,1500),75,(50,200,600,1400,1700,2000)]
prop_cost=[0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,
           200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]

house_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

hotel_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

mortgage_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

chance_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

chest_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

not_props=[0,2,4,7,10,17,20,22,30,33,36,38]
unowned=[]
double=[]
owned=[]

chance_dict={1:"Advance to the nearest utility. If unowned, you may buy it from the bank. If owned, you may buy it from the bank. If owned, throw dice and pay owner ten times the amount thrown",
             2:"Advance to the nearest railroad. If unowned you may buy it from the bank. If owned, pay owner twice the rent to which they are otherwise entitled.",
             3:"Take a trip to Reading Railroad. If you pass go, collect $200.",
             4:"GO TO JAIL. GO DIRECTLY TO JAIL DO NOT PASS GO DO NOT COLLECT $200",
             5:"Go back 3 spaces.",
             6:"Advance to Illinois Avenue. If you pass go, collect $200.",
             7:"Speeding Fine $15",
             8:"Advance to St. Charles Place. If you pass go, collecct $200",
             9:"Your building loan matures, collect $150",
             10:"You have been elected chairman of the board. Pay each player $50",
             11:"Advance to the nearest railroad. If unowned you may buy it from the bank. If owned, pay owner twice the rent to which they are otherwise entitled.",
             12:"Bank pays you dividend of $50",
             13:"Advance to go, collect $200",
             14:"Advance to Boardwalk",
             15:"Get out of jail free. This card may be kept until needed or sold.",
             16:"Make general repairs on all your property. For each house, pay $25, for each hotel, pay $100"}

chest_dict={1:"Get out of jail free. This card may be kept until needed or sold.",
            2:"Income tax refund, collect $20",
            3:"Advance to go. Collect $200",
            4:"School fees. Pay $50",
            5:"Holiday fund matures collect $100",
            6:"Life insurance matures. collect $100",
            7:"You inherit $100",
            8:"Receive $25 consultancy fee",
            9:"You are assessed for street repairs. pay $40 per house and $115 per hotel you own.",
            10:"GO TO JAIL GO DIRECTLY TO JAIL DO NOT PASS GO DO NOT COLLECT $200",
            11:"From sale of stock, you get $50.",
            12:"You have won second prize in a beauty contest. Collect $10",
            13:"Bank error in your favor. collect $200.",
            14:"Doctor's fees. Pay $50",
            15:"It's your birthday! Collect $10 from every player.",
            16:"Hospital fees. Pay $100"}

#functions

def rent(current,roll):
    x=house_list[current]
    y=rent_list[current]
    if type(rent_list[current])==tuple and hotel_list[current]==0:
        return y[x]
    elif hotel_list[current]==1:
        return y[5]
    else:
        return rent_list[current][x]
    
def print_list(p):
    i=0
    while i<len(p):
        print(p[i])
        i=i+1

for i in range(0,40):
    bs=0
    if i in not_props:
        bs=bs+100
    else:
        unowned.append(i)

#Classes
class player():
    free_parking=50
    def __init__ (self, name, properties,position=0, money=1500, jail=False,jail_count=0,jailcard=False):
        self.position=position
        self.money=money
        self.properties=properties
        self.jail=jail
        self.name=name
        self.jail_count=jail_count
        self.jailcard=jailcard

    def railroad(self):
        if self.position==5 or self.position==15 or self.position==25 or self.position==35:
            return True
        else:
            return False

    def roll(self):
        not_props=[0,2,4,7,10,17,20,22,30,33,36,38]
        x=random.randint(1,6)
        y=random.randint(1,6)
        if self.position==10 and self.jail==True and self.jail_count<3:
            if x==y:
                print("You rolled doubles! You are out of jail")
                self.jail=False
            elif self.jail_count==3:
                self.pay_to_free_parking(50)
                self.jail=False
                print("You posted bail after 3 turns")
            else:
                print("You did not roll doubles. You are still in jail until youuse a get out of jail frree, pay bail, or are forced to.")
                self.jail_count=self.jail_count+1
        else:
            if self.position+x+y>=40:
                self.money=self.money+200
            self.position=(self.position+x+y)%40
            print(self.position,board_spaces[self.position])
            if self.position==20:
                print("You earned $",player.free_parking," from free parking!")
                self.money=self.money+player.free_parking
                player.free_parking=50
            elif self.position==30:
                print("\n \n \nYOU ARE IN JAIL FOR 3 TURNS. GET OUT WITH DOUBLES OR POST BAIL OR GET OUT OF JAIL FREE \n \n \n")
                self.position=10
                self.jail=True
            if self.railroad() and self.position not in self.properties and self.position in owned:
                if mortgage_list[self.position]!=0:
                    print("This property is mortgaged. You do not pay rent!")
                self.railroad_rent()
            elif self.utility() and self.position not in self.properties and self.position in owned:
                if mortgage_list[self.position]!=0:
                    print("This property is mortgaged. You do not pay rent!")
                count=-1
                if self==player_1:
                    for i in player_2.properties:
                        if i==12 or i==28:
                            count=count+1
                    print("You owe Player 2 $",(rent_list[player_1.position][count]*(x+y)))
                    player_1.pay_to_player(rent_list[player_1.position][count]*(x+y))
                else:
                    for i in player_1.properties:
                        if i==12 or i==28:
                            count=count+1
                    print("You owe Player 1 $",(rent_list[player_2.position][count]*(x+y)))
                    player_2.pay_to_player(rent_list[player_2.position][count]*(x+y))
            elif self.position not in self.properties and self.position in owned:
                if mortgage_list[self.position]!=0:
                    print("This property is mortgaged. You do not pay rent!")
                else:
                    print('You owe the other player $', rent(self.position,(x+y)))
                    self.pay_to_player(rent(self.position,(x+y)))
            elif self.position in not_props:
                print('You cannot buy',board_spaces[self.position])
                if self.position==4:
                    self.pay_to_bank(200)
                    print("You owe the bank $200")
                elif self.position==38:
                    self.pay_to_free_parking(75)
                    print("You paid $75 to free parking")
            elif self.position in self.properties:
                print("You already own it")
                return()
            else:
                if self.position in self.properties:
                    print("You already own it.")
                    return()
                else:
                    print("Would you like to buy this? It costs ",prop_cost[self.position])
                    x=input("Yes or No or Props(Check Properties) or Money(Check Money)?")
                    if x=="yes" or x=="Yes" or x=="y":
                        self.buy_prop()
                    elif x=="no" or x=="n" or x=="No":
                        pass
                    elif x=="Props" or x=="props" or x=="Props(Check Properties)" or x=="p":
                        print(self.prop_names())
                        x=input("Yes or No or Props(Check Properties)?")
                        if x=="yes" or x=="Yes" or x=="y":
                            self.buy_prop()
                        elif x=="no" or x=="n" or x=="No":
                            pass
                        else:
                            print("You did not return a valid answer and can no longer buy it")
                    elif x=="Money" or x=="m" or x=="money" or x=="Check Money":
                        print(self.money)
                        x=input("Yes or No or Props(Check Properties)?")
                        if x=="yes" or x=="Yes" or x=="y":
                            self.buy_prop()
                        elif x=="no" or x=="n" or x=="No":
                            pass
                        elif x=="Props" or x=="props" or x=="Props(Check Properties)" or x=="p":
                            print(self.prop_names())
                            x=input("Yes or No?")
                            if x=="yes" or x=="Yes" or x=="y":
                                self.buy_prop()
                            elif x=="no" or x=="n" or x=="No":
                                pass
                            else:
                                print("You did not return a valid answer and can no longer buy it")
                        else:
                            print("You did not return a valid answer and can no longer buy it")
                    else:
                        print("You did not return a valid answer and can no longer buy it")
        if x==y:
            global double
            double.append(1)
        else:
            double=[]
    
    def pay_to_player(self,amount):
        if self==player_1:
            self.money=self.money-amount
            player_2.money=player_2.money+amount
        else:
            player_2.money=player_2.money-amount
            player_1.money=player_1.money+amount
    def buy_prop(self):
        if self.position in self.properties:
            print("You already own this")
        else:
            self.money=self.money-prop_cost[self.position]
            self.properties.append(self.position)
            unowned.remove(self.position)
            owned.append(self.position)
            print("You have bought ",board_spaces[self.position])

    def pay_to_bank(self,amount):
        self.money=self.money-amount
    
    def pay_to_free_parking(self,amount):
        self.money=self.money-amount
        player.free_parking=player.free_parking+amount

    def buy_house(self):
        self.properties.sort()
        print_list(self.properties)
        x=int(input("Which property did you want to put houses on?(Insert number of space)"))
        p=0
        total_houses=32
        availablehouses=total_houses-sum(house_list)
        for i in range(0,8):
            if x in list(full_set.values())[i]:
               p=i
            else:
               pass
        f=list(full_set.values())[p]
        if house_list[x]==4:
            print("You can't buy anymore houses")
        elif availablehouses==0:
            print("There are no houses available to buy at the moment")
        elif list_in_list(f, self.properties):
            for i in f:
                if (house_list[x]-house_list[i])==1 or (house_list[x]-house_list[i])>1:
                    print("You cannot buy houses on this property until all properties in this set are of same number")
            if x in range(0,10):
                    self.pay_to_bank(50)
                    total_houses=total_houses-1
                    house_list[x]=house_list[x]+1
                    return (board_spaces[x],house_list[x])
            elif x in range (11,20):
                    self.pay_to_bank(100)
                    total_houses=total_houses-1
                    house_list[x]=house_list[x]+1
                    return (board_spaces[x],house_list[x])
            elif x in range (21,30):
                    self.pay_to_bank(150)
                    total_houses=total_houses-1
                    house_list[x]=house_list[x]+1
                    return (board_spaces[x],house_list[x])
            elif x in range(31,40):
                    self.pay_to_bank(200)
                    total_houses=total_houses-1
                    house_list[x]=house_list[x]+1
                    return (board_spaces[x],house_list[x])
        else:
            print("You don't have the set")

    def buy_hotel(self):
        self.properties.sort()
        print_list(self.properties)
        x=int(input("Which property did you want to put a hotel on?(Insert number of space)"))
        p=0
        for i in range(0,8):
            if x in list(full_set.values())[i]:
                p=i
        f=list(full_set.values())[p]
        f.remove(x)
        total_hotels=12
        availablehotels=total_hotels-sum(hotel_list)
        for i in f:
            if (house_list[x]-house_list[i])>=1 or hotel_list[i]==1:
                print("You cannot buy hotel on this property until all properties in this set are of house=4")
        if house_list[x]==4 and availablehotels!=0 and hotel_list[x]<=1:
            if x in range(0,10):
                self.pay_to_bank(50)
                hotel_list[x]=hotel_list[x]+1
                house_list[x]=house_list[x]-4
                return (board_spaces[x],hotel_list[x])
            elif x in range (11,20):
                self.pay_to_bank(100)
                hotel_list[x]=hotel_list[x]+1
                house_list[x]=house_list[x]-4
                return (board_spaces[x],hotel_list[x])
            elif x in range (21,30):
                selfpay_to_bank(150)
                hotel_list[x]=hotel_list[x]+1
                house_list[x]=house_list[x]-4
                return (board_spaces[x],hotel_list[x])
            elif x in range(31,40):
                self.pay_to_bank(200)
                hotel_list[x]=hotel_list[x]+1
                house_list[x]=house_list[x]-4
                return (board_spaces[x],hotel_list[x])
        
    def sell_house(self):
        self.properties.sort()
        print_list(self.properties)
        x=int(input("Which property did you want to take a house off of?(Insert number of space)"))
        p=0
        for i in range(0,8):
            if x in list(full_set.values())[i]:
               p=i
            else:
               pass
        f=list(full_set.values())[p]
        if house_list[x]!=0:
           for i in f:
                if (house_list[x]-house_list[i])==-1 or (house_list[x]-house_list[i])<-1:
                    print("You cannot sell houses on this property until all properties in this set are of same number")
                else:
                    house_list[x]=house_list[x]-1
                    if x in range(0,10):
                        self.money=self.money+25
                        return (board_spaces[x],house_list[x])
                    elif x in range (11,20):
                        self.money=self.money+50
                        return (board_spaces[x],house_list[x])
                    elif x in range (21,30):
                        self.money=self.money+75
                        return (board_spaces[x],house_list[x])
                    elif x in range(31,40):
                        self.money=self.money+100
                        return (board_spaces[x],house_list[x])
        else:
            print("There are no houses on that property")
        

    def sell_hotel(self):
        self.properties.sort()
        print_list(self.properties)
        x=int(input("Which property did you want to take the hotel off of?(Insert number of space)"))
        p=0
        for i in range(0,8):
            if x in list(full_set.values())[i]:
                p=i
        f=list(full_set.values())[p]
        if hotel_list[x]==0:
            print("You do not have a hotel on this space")
        if hotel_list[x]==1:
            hotel_list[x]=hotel_list[x]-1
            house_list[x]=house_list[x]+4
            if x in range(0,10):
                self.money=self.money+25
                return (board_spaces[x],hotel_list[x])
            elif x in range (11,20):
                self.money=self.money+50
                return (board_spaces[x],hotel_list[x])
            elif x in range (21,30):
                self.money=self.money+75
                return (board_spaces[x],hotel_list[x])
            elif x in range(31,40):
                self.money=self.money+100
                return (board_spaces[x],hotel_list[x])
            print("You removed a hotel from  ",board_spaces[self.position], "and now have 4 houses there")
        
            
    def simulate(self,rolls):
        for i in range(1,rolls):
            self.roll()

    def railroad_rent(self):
        count=-1
        if self==player_1:
            for i in player_2.properties:
                if i==5 or i==15 or i==25 or i==35:
                    count=count+1
            print("You owe Player 2 $",rent_list[player_1.position][count])
            player_1.pay_to_player(rent_list[player_1.position][count])
        elif self==player_2:
            for i in player_1.properties:
                if i==5 or i==15 or i==25 or i==35:
                    count=count+1
            print("You owe Player 1 $", rent_list[player_2.position][count])
            player_2.pay_to_player(rent_list[player_2.position][count])
            
    def railroad(self):
        if self.position==5 or self.position==15 or self.position==25 or self.position==35:
            return True
        else:
            return False
        
    def utility(self):
        if self.position==12 or self.position==28:
            return True
        else:
            return False
        
    def prop_names(self):
        for i in self.properties:
            print(board_spaces[i])

    def mortgage(self):
        self.properties.sort()
        for i in self.properties:
            if mortgage_list[i]==0:
                print(i,board_spaces[i])
        x=int(input("What property would you like to mortgage? (Input number)"))
        if x in self.properties:
            self.money=self.money+(prop_cost[x]/2)
            mortgage_list[x]=1
            print("You have mortgaged ",board_spaces[x])
        elif mortgage_list[x]==1:
            print("You have already mortgaged this property.")
        else:
            print("You do not own that property.")

    def unmortgage(self):
        for i in self.properties:
            if mortgage_list[i]==1:
                print(i,board_spaces[i])
        x=int(input("Which of these mortgaged properties would you like to unmortgage?"))
        if x in self.properties:
            mortgage_list[x]=0
            self.money=self.money-(1.1*(prop_cost[x]/2))
            print("You have unmortgaged ", board_spaces[x])
        else:
            print("You do not own that property.")
    
    def chance(self):
        if sum(chance_list)==16:
            for i in range(0,15):
                chance_list[i]=0
        j=random.randint(1,16)
        if chance_list[j-1]==0:
            print(list(chance_dict.items())[j-1])
            chance_list[j-1]=1
            if j==1:
                if self.position>12:
                    self.position=28
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You will now roll and pay owner 10 times that amount")
                        f=random.randint(1,6)
                        m=random.randint(1,6)
                        self.pay_to_player(10*(f+m))
                        print("You paid the other player $",10*(f+m))
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                        else:
                            pass
                elif self.position>28:
                    self.money += 200
                    print('You passed go. Collect $200.')
                    self.position=12
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You will now roll and pay owner 10 times that amount")
                        f=random.randint(1,6)
                        m=random.randint(1,6)
                        self.pay_to_player(10*(f+m))
                        print("You paid the other player $",10*(f+m))
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                        else:
                            pass
                elif self.position<12:
                    self.position=12
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You will now roll and pay owner 10 times that amount")
                        f=random.randint(1,6)
                        m=random.randint(1,6)
                        self.pay_to_player(10*(f+m))
                        print("You paid the other player $",10*(f+m))
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                        else:
                            pass
            elif j==2 or j==11:
                if self.position>35:
                    self.money=self.money+200
                    self.position=5
                    print("You passed Go")
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()   
                elif self.position<5:
                    self.position=5
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                elif self.position>5 and self.position<15:
                    self.position=15
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                elif self.position>15 and self.position<25:
                    self.position=25
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                elif self.position>25 and self.position<35:
                    self.position=35
                    print("Your new position is ",self.position)
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
            elif j==3:
                if self.position>5:
                    print("You passed go")
                    self.money=self.money+200
                    self.position=5
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                        else:
                            pass
                else:
                    self.position=5
                    if self.position not in self.properties and self.position in owned:
                        print("You owe the other player rent")
                        self.railroad_rent()
                    else:
                        print("No one owns this property")
                        print("Would you like to buy it? It costs $",prop_cost[self.position])
                        w=input("Yes or No?")
                        if w=="Yes" or w=="yes" or w=="y":
                            self.buy_prop()
                        else:
                            pass
            elif j==4:
                self.position=10
                self.jail=True
                print("You are in jail until you use a get out of jail free, post bail, or are forced to post bail")
            elif j==5:
                self.position=self.position-3
                print("You have moved back 3 spaces onto ",board_spaces[self.position])
                if self.position not in self.properties and self.position in owned:
                    if mortgage_list[self.position]!=0:
                        print("This property is mortgaged. You do not pay rent!")
                    else:
                        print('You owe the other player $', rent(self.position,(x+y)))
                        self.pay_to_player(rent(self.position,(x+y)))
                elif self.position in not_props:
                    print('You cannot buy',board_spaces[self.position])
                    if self.position==4:
                        self.pay_to_bank(200)
                        print("You owe the bank $200")
                    elif self.position==38:
                        self.pay_to_free_parking(75)
                        print("You paid $75 to free parking")
                elif self.position in self.properties:
                    print("You already own it")
                else:
                    if self.position in self.properties:
                        print("You already own it.")
                    else:
                        print("Would you like to buy this? It costs ",prop_cost[self.position])
                        x=input("Yes or No or Props(Check Properties) or Money(Check Money)?")
                        if x=="yes" or x=="Yes" or x=="y":
                            self.buy_prop()
                        elif x=="no" or x=="n" or x=="No":
                            pass
                        elif x=="Props" or x=="props" or x=="Props(Check Properties)" or x=="p":
                            print(self.prop_names())
                            x=input("Yes or No or Props(Check Properties)?")
                            if x=="yes" or x=="Yes" or x=="y":
                                self.buy_prop()
                            elif x=="no" or x=="n" or x=="No":
                                pass
                            else:
                                print("You did not return a valid answer and can no longer buy it")
                        elif x=="Money" or x=="m" or x=="money" or x=="Check Money":
                            print(self.money)
                            x=input("Yes or No or Props(Check Properties)?")
                            if x=="yes" or x=="Yes" or x=="y":
                                self.buy_prop()
                            elif x=="Props" or x=="props" or x=="Props(Check Properties)" or x=="p":
                                print(self.prop_names())
                                x=input("Yes or No?")
                                if x=="yes" or x=="Yes" or x=="y":
                                    self.buy_prop()
                                else:
                                    print("You did not return a valid answer and can no longer buy it")
                            else:
                                print("You did not return a valid answer and can no longer buy it")
                        else:
                            print("You did not return a valid answer and can no longer buy it")
            elif j==6:
                if self.position>24:
                    self.money=self.money+200
                    print("You passed go and got $200")
                    self.position=24
                    print("Your new position is ",board_spaces[self.position])
                    if self.position not in self.properties and self.position in owned:
                        if mortgage_list[self.position]!=0:
                            print("This property is mortgaged. You do not pay rent!")
                        print('You owe the other player $', rent(self.position,(1)))
                        self.pay_to_player(rent(self.position,(1)))
                    elif self.position in self.properties:
                        print("You already own ",board_spaces[self.position])
                    else:
                        print("This property is unowned. Would you like to buy it? It costs ",prop_cost[self.position])
                        x=input("Yes or No?")
                        if x=="Yes" or x=="yes" or x=="y":
                            self.buy_prop()
                elif self.position<24:
                    self.position=24
                    print("Your new position is ",board_spaces[self.position])
                    if self.position not in self.properties and self.position in owned:
                        if mortgage_list[self.position]!=0:
                            print("This property is mortgaged. You do not pay rent!")
                        print('You owe the other player $', rent(self.position,(1)))
                        self.pay_to_player(rent(self.position,(1)))
                    elif self.position in self.properties:
                        print("You already own ",board_spaces[self.position])
                    else:
                        print("This property is unowned. Would you like to buy it? It costs ",prop_cost[self.position])
                        x=input("Yes or No?")
                        if x=="Yes" or x=="yes" or x=="y":
                            self.buy_prop()
            elif j==7:
                self.pay_to_free_parking(15)
                print("You paid $15 to free parking")
            elif j==8:
                if self.position>11:
                    print("You passed go and got $200")
                    self.money=self.money+200
                    self.position=11
                    print("Your new position is ",board_spaces[self.position])
                    if self.position not in self.properties and self.position in owned:
                        if mortgage_list[self.position]!=0:
                            print("This property is mortgaged. You do not pay rent!")
                        print('You owe the other player $', rent(self.position,(1)))
                        self.pay_to_player(rent(self.position,(1)))
                    elif self.position in self.properties:
                        print("You already own ",board_spaces[self.position])
                    else:
                        print("This property is unowned. Would you like to buy it? It costs ",prop_cost[self.position])
                        x=input("Yes or No?")
                        if x=="Yes" or x=="yes" or x=="y":
                            self.buy_prop()
                elif self.position<11:
                    self.position=11
                    print("Your new position is ",board_spaces[self.position])
                    if self.position not in self.properties and self.position in owned:
                        if mortgage_list[self.position]!=0:
                            print("This property is mortgaged. You do not pay rent!")
                        print('You owe the other player $', rent(self.position,(1)))
                        self.pay_to_player(rent(self.position,(1)))
                    elif self.position in self.properties:
                        print("You already own ",board_spaces[self.position])
                    else:
                        print("This property is unowned. Would you like to buy it? It costs ",prop_cost[self.position])
                        x=input("Yes or No?")
                        if x=="Yes" or x=="yes" or x=="y":
                            self.buy_prop()
            elif j==9:
                self.money=self.money+150
                print("The bank gave you $150")
            elif j==10:
                self.pay_to_player(50)
                print("You paid the other player $50")
            elif j==12:
                self.money=self.money+50
                print("The bank paid you $50")
            elif j==13:
                self.position=0
                self.money=self.money+200
                print("You are now on GO and have collected $200")
            elif j==14:
                if self.position==39:
                    self.money=self.money+200
                    print("You are still on Boardwalk")
                    if self.position not in self.properties and self.position in owned:
                        if mortgage_list[self.position]!=0:
                            print("This property is mortgaged. You do not pay rent!")
                        print('You owe the other player $', rent(self.position,(1)))
                        self.pay_to_player(rent(self.position,(1)))
                    elif self.position in self.properties:
                        print("You already own ",board_spaces[self.position])
                    else:
                        print("This property is unowned. Would you like to buy it? It costs ",prop_cost[self.position])
                        x=input("Yes or No?")
                        if x=="Yes" or x=="yes" or x=="y":
                            self.buy_prop()
                elif self.position<39:
                    self.position=39
                    if self.position not in self.properties and self.position in owned:
                        if mortgage_list[self.position]!=0:
                            print("This property is mortgaged. You do not pay rent!")
                        print('You owe the other player $', rent(self.position,(1)))
                        self.pay_to_player(rent(self.position,(1)))
                    elif self.position in self.properties:
                        print("You already own ",board_spaces[self.position])
                    else:
                        print("This property is unowned. Would you like to buy it? It costs ",prop_cost[self.position])
                        x=input("Yes or No?")
                        if x=="Yes" or x=="yes" or x=="y":
                            self.buy_prop()
            elif j==15:
                self.jailcard=True
                print("You now have a get out of jail free card. It may be kept until needed or sold")
            elif j==16:
                    fee=0
                    count=0
                    for prop in self.properties:
                        if house_list[prop]==5:
                            fee=fee+100
                        else:
                            count=count+house_list[prop]
                    fee=fee+(count*25)
                    self.pay_to_bank(fee)
                    print("You paid the bank ",(fee+(count*25)))
            else:
                print("This is my code bugging out for some reason")
        else:
            self.chance()

    def chest(self):
        if sum(chest_list)==16:
            for i in range(0,15):
                chest_list[i]=0
        j=random.randint(1,16)
        if chest_list[j-1]==0:
            print(list(chest_dict.items())[j-1])
            chest_list[j-1]=1
            if j==1:
                self.jailcard=True
                print("You now have a get out of jail free card. It may be kept until needed or sold")
            elif j==2:
                self.money=self.money+20
                print("The bank paid you $20")
            elif j==3:
                self.position=0
                self.money=self.money+200
                print("You are now on GO and have collected $200")
            elif j==4:
                self.pay_to_free_parking(50)
                print("You put $50 in Free Parking")
            elif j==5:
                self.money=self.money+100
                print("The bank paid you $100")
            elif j==6 or j==7:
                self.money=self.money+100
                print("The bank paid you $100")
            elif j==8:
                self.money=self.money+25
                print("The bank paid you $25")
            elif j==9:
                fee=0
                count=0
                for prop in self.properties:
                    if house_list[prop]==5:
                        fee=fee+115
                    else:
                        count=count+house_list[prop]
                fee=fee+(count*40)
                self.pay_to_bank(fee)
                print("You paid the bank ",(fee+(count*40)))
            elif j==10:
                self.position=10
                self.jail=True
                print("You are in jail until you use a get out of jail free, post bail, or are forced to post bail")
            elif j==11:
                self.money=self.money+50
                print("The bank paid you $50")
            elif j==12:
                self.money=self.money+10
                print("The bank paid you $10")
            elif j==13:
                self.money=self.money+200
                print("The bank paid you $200")
            elif j==14:
                self.pay_to_free_parking(50)
                print("You paid $50 to free parking")
            elif j==15:
                if self==player_1:
                    player_1.money+=10
                    player_2.money-=10
                else:
                    player_1.money-=10
                    player_2.money+=10
            elif j==16:
                self.pay_to_free_parking(100)
                print("You paid $100 to Free Parking")
        else:
            self.chest()
                
                
                

    def turn(self):
        x=0
        for i in range(0,len(list(opts.items()))):
            print(list(opts.items())[i])
        while x !=1: 
            try:
                x=int(input("\nWhat would you like to do?"))
                if x==1:
                    self.roll()
                    if self.position==7 or self.position==22 or self.position==36:
                        self.chance()
                    elif self.position==2 or self.position==17 or self.position==33:
                        self.chest()
                elif x==12:
                    print("This was a feature I was hoping to make")
                elif x==5:
                    self.buy_house()
                elif x==7:
                    self.buy_hotel()
                elif x==6:
                    self.sell_house()
                elif x==8:
                    self.sell_hotel()
                elif x==10:
                    self.mortgage()
                elif x==9:
                    if self.jail:
                        self.pay_to_free_parking(50)
                        self.jail=False
                        print("You posted bail")
                    else:
                        print("You are not in jail")
                elif x==13:
                    print("This was an additional feature I was hoping to make")
                elif x==4:
                    self.properties.sort()
                    self.prop_names()
                elif x==2:
                    print(self.money)
                elif x==14:
                    quit()
                elif x==3:
                    print(self.position,board_spaces[self.position])
                elif x==11:
                    self.unmortgage()
                elif x==15:
                    if self.jailcard:
                        self.jail=False
                        self.jailcard=False
                        print("You have used your card and are out of jail")
                    else:
                        print("You do not have that card")
                else:
                    print("Not a valid action")
            except:
                print(sys.exc_info()[0])
                print("You cannot put that value. Try again")
                self.turn()
        while self.money<0:
            for i in range(0,7):
                print(list(broke_opts.items())[i])
            x=int(input("You're broke! What would you like to do?"))
            if x==1:
                print("This was a feature I was hoping to make")
            if x==2:
                self.sell_house()
            elif x==3:
                self.sell_hotel()
            elif x==4:
                self.mortgage()
            elif x==5:
                print(self.money)
            elif x==6:
                self.properties.sort()
                print(self.properties)
            elif x==7:
                break
            
full_set={'brown':[1,3],'light blue':[6,8,9],'pink':[11,13,14],'orange':[16,18,19],'red':[21,23,24],'yellow':[26,27,29],
          'green':[31,32,34],'dark blue':[37,39]}
name_1=input("What is your name?")
name_2=input("What is the other player's name?")
player_1=player(name_1,[])
player_2=player(name_2,[])

opts={"1":"Move","2":"Check Money","3":"Check Space","4":"Check Properties","5":"Buy House",
      "6":"Sell House","7":"Buy Hotel","8":"Sell Hotel","9":"Post Bail","10":"Mortgage",
      "11":"Unmortgage","12":"Trade","13":"Save Game","14":"End Game/Flip Table Over","15":"Use Get Out of Jail Free Card"}

broke_opts={1:"Trade",2:"Sell House",3:"Sell Hotel",4:"Mortgage",
            5:"Check Money",6:"Check Properties",7:"Give Up"}
def list_in_list(list1,list2):
    for item in list1:
        if item in list2:
            pass
        else:
            return False
    return True

while player_1.money>=0 and player_2.money>=0:
    double=[]
    print("\n", player_1.name, "'s Turn \n")
    player_1.turn()
    if len(double)==1:
        print("\nStill", player_1.name,"'s Turn \n")
        player_1.turn()
    elif len(double)==2:
        print("\nStill", player_1.name,"'s Turn \n")
        player_1.turn()
    elif len(double)==3:
        print("\nGO TO JAIL> GO DIRECTLY TO JAIL DO NOT PASS GO DO NOT COLLECT 300 \n")
        player_1.position=10
        player_1.jail=True
    print("\n", player_2.name,"'s Turn \n")
    player_2.turn()
    if len(double)==1:
        print("\nStill ", player_2.name,"'s Turn \n")
        player_2.turn()
    elif len(double)==2:
        print("\nStill ", player_2.name,"'s Turn \n")
        player_2.turn()
    elif len(double)==3:
        print("\nGO TO JAIL> GO DIRECTLY TO JAIL DO NOT PASS GO DO NOT COLLECT 300 \n")
        player_2.position=10
        player_2.jail=True

if player_1.money>player_2.money:
   print( player_1.name,"wins!")
else:
    print(player_2.name,"wins!")
    
    
	


        
