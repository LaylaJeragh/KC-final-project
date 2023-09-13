import datetime
import random
import webbrowser
import subprocess


# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# Function to perform a web search using the default browser
def search(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

# Function to create a note using the default text editor
def create_note():
    print("What would you like to write in the note?")
    content = input()
    
    # Save the note to a file or perform any other desired action
    filename = "note.txt"
    
    with open(filename, "w") as file:
        file.write(content)
    
    print("Note saved!")

# Main program loop
while True:
    print("\nHow can I assist you?")
    
    # Get user input
    command = input().lower()

    jokes = ["Why do we tell actors to “break a leg? Because every play has a cast.","Why couldn't the sailor learn the alphabet? Because he always got lost at C.","What did the shark say when he ate the clownfish? This taste funny.","Why did the bicycle collapse? It was two tired.","My boss told me to have a good day....so I went home.","Today at the bank, an old lady asked me to help check her balance....so I pushed her","An apple a day can really keep the doctor away.... but only if you aim it well","why don't they play UNO in the jungle.... because there is too many cheetahs.","Why should you always knock the fridge door before opening it....in case there is a salad dressing."]
    poems = ["Risk, by Anaïs Nin","Stopping by Woods on a Snowy Evening , by Robert Frost.","Hope is the thing with feathers, by Emily Dickinson.","The Peace of Wild Things, by Wendell Berry.","The Summer Day, by Mary Oliver.","The Guest House, by Rumi.","Awaking in New York, by Maya Angelou","This Room, John Ashberry","The sick rose, William Blake"]
    short_stories = ["After a swim (kids)","The Ant and the pen (kids)","The Ugly Duckling (kids)","The tortise and the hare (kids)","Little red riding hood (kid)","The ant and grasshopper (kids)","the turtle and the monkey (kids)","The nightingale (kids)","Thumbelina (kids)","The fishermen and his wife (kid)", "The sky is fallig (kid)"," Hansel and Gretel (Kid)", "The Haunted Mind (adult)","The killers (adult)", "The Garden Party (adult)","the selfish giant (adult)","The tell-tale heart (adult)","The yellow wallpaper (adult)","The Golden Egg (Best Moral Story)"]
    books = ["Harry Potter Series","Good Girl Guide to Murder series","The Lord of the Rings series","To kill a mocking bird", "Lock the doors","The book theif","The Alchemist", "The Fualt in Our Stars", "My Fault", "Five Feet Apart", "The Hobbit","Twilight","A Wrinkle in Time", "Little Women", "We were liars", "Verity", "Lord of Flies", "Divergent","One of us is lying series","A Monster Calls","Amulet series","Red, White & Royal Blue","It Ends with Us","THey both die at the end","Book Lovers","A touch of Darkness", "Icebreaker","The Love Hypnothesis","It happened One Summer","Shatter Me","Fourth Wing","It Starts With Us","The Midnight Library","The Inheritance Games","The Seven Husbands of Evelyn Hugo","A court of Thorns and Roses","The Silent Patient","If HE Had Been With Me","Shadow and Bone","Act your Age","People We Meet On Vacation","the Atlas Six","Delilah Green doesn't care","The School of Good and Evil Series","The Beast Within","Poor Unfortunate Soul","Mother Knows Best","Mistress of all evil","Red Queen Series","Kingdom of Wicked Series","All thus time","The Family Upstairs","The Family Remains","The Girl in the Castle","Freeks","Dragon Pearl","Anne of Green Gables","The Little Stranger","Missing Me","Missing Sister","Missing Girl","Demon in the woods","13 Reasons Why","GooseBumps Series","The things we leave unfinished","If Cats Disappered from the world","The forty rules of love","Salt to the sea","All The bright places","Sea ofg Strangers","Five Nights At Freddy's Series","The Book Theif","The kill order","A discovery of witches","Thorne of Glass Series","Assassin Blade","All The Light We Cannot See", "Library of Soul","Heir of Fire","The Promise Neverland Series","Love and Gelato Series","The Girl who drank The Moon","The Babysitter Club Series","To Kill A Kingdom","Sky In The Deep","Ending: The Last","Love & War","The Land of Stories","The Girl On The Train","Fear Street Series","Girl in Pecies","Treasure Island","The Kiss Of Deception","Slated","The Queen Gambet","The Bell Jar","Heartless","The Art of War","These Broken Stars","The happiness project","The Giver","Marvel Comics","DC Comics","X-Mex Comics","Heros of Olympus Series","The Maze Runner","Sapiens","A Curse so Dark and Lonely","The Raven Boys","Frankenstein","The Stationery Shop","Heartless","The Green Mile","The Siren","Their Fractured Light Series","The ABC Murders","Children of Blood and Bone"]
    draw = ["Cityscapes","Landscapes","Cartoon Characters","Vehicles","3D Forms","Ghosts","Horses","Butterflies","Race Cars","Pirate Ship","Palm Trees","Tulips","Pine Cones","Space Ships","Box of candy","Sunflowers in a vase","Imaginery Creatures","Magistic Creatures","Hybrid Animal","Portraits","Favorite cartoon character","Favorite movie or tv-show character","Cool Animal","Diffrent types of flowers","Cute animals","Glasses","House plant","A Cup or a saucer","Eyes","Celebrities","Fruits","Snakes","Skulls","Fish","Clovers","Line Drawing","Hearts","Leaves","Gems","Diamonds","Ballons","Candy Canes","Gifts","Cactus","Beaches","Lakes","Planets","Ice Cream Cones","Anime","Dragons","Wolves","SpaceShips","Surfboards","Super Heroes","Spider Webs","Instruments","Gnomes","Bunnies","Birds","Squirrels","Kittens","Puppies","Bugs","Sea Animals","Hallaween","Dinosaurs","Wild Flowers","Crowns","Boats","Monsters","Eagles","Dragonflies","Fashion","Hot Air Ballons","One Line Art","Favorite Things","Your friend or friends/Family member or members"]
    paint = ["Cityscapes","Landscapes","Cartoon Characters","Vehicles","3D Forms","Ghosts","Horses","Butterflies","Race Cars","Pirate Ship","Palm Trees","Tulips","Pine Cones","Space Ships","Box of candy","Sunflowers in a vase","Imaginery Creatures","Magistic Creatures","Hybrid Animal","Portraits","Favorite cartoon character","Favorite movie or tv-show character","Cool Animal","Diffrent types of flowers","Cute animals","Glasses","House plant","A Cup or a saucer","Eyes","Celebrities","Fruits","Snakes","Skulls","Fish","Clovers","Line Drawing","Hearts","Leaves","Gems","Diamonds","Ballons","Candy Canes","Gifts","Cactus","Beaches","Lakes","Planets","Ice Cream Cones","Anime","Dragons","Wolves","SpaceShips","Surfboards","Super Heroes","Spider Webs","Instruments","Gnomes","Bunnies","Birds","Squirrels","Kittens","Puppies","Bugs","Sea Animals","Hallaween","Dinosaurs","Wild Flowers","Crowns","Boats","Monsters","Eagles","Dragonflies","Fashion","Hot Air Ballons","One Line Art","Favorite Things","Your friend or friends/Family member or members"]
    games = ["Fortnight","Call of Duty","Mario Games","God of War","Disco Elysium","Over Watch","Half-life:Alyx","Divinity","Final Fantasy","Outer Wilds","Stardew Vally","Genshin Impact","Animal Crossing","Prey","Baldur's Gate 3","Resident Evil","Doom Eternals","Dishonored","Batman","Alien","The Legend of Zelda","Super Smash Bros","Deathloop","The Sims","Skyram","The Elder Scrolls","Starfield","Psychonauts","Rocket League", "Dota","Hollow Knight","Control","Apex Legends","Forza horizon","Elden Ring","Red Dead Redemption","The Witcher","Hades","XCOM","Grand Thef Auto","Crusader Kings","Minecraft","Civilization","Slay the Spire","FTL","Portal","Destiny","Into The Breach","PUBG","Counter-Strike","League of Legends","Pokemon","Pokemon Go","Wii Play","Final Fantasy","Super Mario world","Super Mario Bros","Kinect Adventures","Pac-Man","Pokemon Sword and Sheild","Sonic the Hedghog","Mario Kart","BorderLands","God of war"," Duck of Hunt","Super Mario Odyssey","Roblex","Tetris","Hearthstone","The Walking Dead"]
    game_projects = ["Pac-Man","Mario Game","Easy POng Game","Cross the road game","Jumping game","Whack-A-Mole","Tic-Tac-Toe","Maze Game","Racing Game","Quiz Game","Memory Game","Pong Game","Snake game","Murder Mystery","War Games","rock Paper Scissors","Hangman","Adventure Game","Bingo","Puzzels","Roblox Games","Tycoons","MineCraft world","AR or VR Games","Jungle themed game like Jurassic World/Park","Hallaween Games","Scary Games like five nights at freddy's","Zombie theme games like walking dead","Story Games","Mystery story game","Drama Story game","Sport Games","FootBall Games","BasketBall Games","Bowling Game","Tennise Game","Hockey Games","Archery Games","Smart watch Games","Mental Health Games","Fantasy and Sci-Fi Games","Educational Games.","Kids Games","Arcade Games","Animal Racing Game like hourse riding","Salon Games","Cooking games","Candy Crush Games","Charades","Ludo games","Chess Game","Snake and Ladder Game","Digital Card Games","Digital Board Games","Team Based Games","Zombie City","Vehicle Battle Games"]
    python_projects = ["Code Generator","Calculator","Interactive Quiz","Number Guessing Game","Food Ordering App","Profitable Apps","Interactive Games","Heavy Traffic Indicator","Story Telling","Cars for sale","Apartment for sale","Analize data","URL Shortener","Address book","Password Generator","Alarm clock","Jobs to find based on what you are searching for.","Note App","Your own Wikipedia expolrer","Build a chat Bot","Program a robot","Stock Market predictor","Image Generator and recognition","Interactive Map","Email Slicer","Google Image downloader","GIF Creator","Games(Check Game projects)","AI","Speed typing test","Library Managment System","Converter(celsius to fahrenheit/ Miles to Kilometer/etc)"]
    web_projects = ["Skin Care Shop","Multi-WebPage website","Job finder website","Blog","Membership websites","Online Learning websites","Online booking systems","Food ideas to cook","Dessert to bake","Interveiw Site","History website","DIY Ideas website","Sell Handmade Items","Health care Shop"," Mental Health website","Realstate and property listing","Physical Health Website","Interor Design Website","Portfrolio and personal website","News and media outlets","Gaming website","Online shops","website like Etsy where users make mini shops in your website","Movies and tv-shows website"]
    flutter_projects = ["Calculator App","Tic tac toe game","weight tracker","Hangman game","Podcast Player","e-commerce app","Pokedex app","Habit Tracker","Skype clone","Book search app","Netflex Clone","Telegram Clone","Cryptocurrency App","Google Clone","Travel Plan App","Calories Traking App","Home Budgting App","Digtal Magazine App","Calculator","Blog App","Social media app"]
    kid_books = ["The Very Hungry Caterpillar","where the wild things are","The tale of peter rabbit","Charlottle's Web","You're my little pumpkin","Winnie the pooh","The very ugly bug","Matilda","Peter pan","Cinderella","Mulam","The Little Mermaid","Beauty and the beast","Aladdin","Charlie and the chocolate factory","Snow white","Brother Grimm books","Dr.Suess books","Little Men books","Little women books","Captain Underpants","Horrid Henry","tinker bell","Charlie and Lola","Frozen","The Three Little Pigs","The secret garden","Knight Owl","The day the crayon quit","Dragons love tacos","Busy Busy Town","I love strawberies","Curious George","MailDuck","Llama llama red pjamas"]
    business_ideas = ["Software training","Home-made store","Pet sitting","Babysitting","Resturant","Cafe","Digital resturant","Digtal Cafe","Dessert","Online Dessert shop","socail media managment","Yard work","Sell on Ebay","Virtual Assistant Service","Web Design Agency","Sell Online Courses","Video Editor","Photo Editor","Home tutoring","Online Tutoring","House sitting","Bookkeeping","Dog walking Business","Freelance Writing Business","Luxury Branding","Sustainabitity Product","Online coaching","Online Reselling","Tshirt Printing","Heat press Items","Cleaning Services","Online teaching","Online booking","Consulting","Medical Courier Service","App Develper","Transcript Services","Professional organizing","Freelance copy writing","Content writing","Home Care service","Translation Service","Digital marketing","Own a Food truck","Lawn care service",'RideShare Driving',"Taxi service","RealEstate","Graphic Design","DropShipping","Personal Training(online or in person)","Resume Writing","Host a Pod-Cast","Launch a newsletter","Event Catering"]
    movies = ["Forest Gump","The Dark Knight","The God Father","The Shawshank Redemption","Star waes Series","Marvel Movies","Transformer Movies","DC Movies","Pulp Fiction","Ms Doubfire","The Lord Of The Rings movies","Back to the future","Great Expectation","Death on the Nile","The Lion King","Disney Princess movies","Disney cartoon movies","Titanic","Avatar movies","Inception","Shutter Island","Nimona","School of good and evil","Jurassic Park movies","Jurassic World movies","Terminator","The Matrix","Saving Pirate island","Treasure Island","Atlantas","2001","65","FIght club","Good Fellas","The wizard of Oz","Toy Story Movies","Up","Grave of the Fireflies","Monster Inc","The Sponge Bob Movie","Spirt","Inside Out","The Fox and the Hound","Bambi","An american tail","Rugrats","The Iron Giant","BFG","How To Train Your Dragon Movies","Pokemon movies","The zprince of Egypt","Watership Down","Ratatouille","The Land Before Time","Dumbo","Wall-e","The Plague Dogs","All Dogs Go to Heaven","Lady and the Tramp","Wreck-it-Ralph","The Good Dinosaur","Charlotte's Web","Spider-Man Movies(Cartoon andreal actors)","Guardians of the Galaxy","Oppenheimer","Mission Impossible","Indiana Jones Movies","The Flash","The Little Mermaid","Fast X","Elemental","Meg","Ruby Gilman Teenage Kraken","Ninja Turtle Movies (Cartoon and real actors)","The super Mario Bros","Insidious","Past Lives","Hypnotic","The Exorcist","The Shining","A Nightmare on elm Street","Fear Streat","The Conjuring","Halloween","The ring","The Grudge","Friday the 13th","FNAF","Saw","Psycho","Paranormal Activity","It","Case 39","Stranger","Jaws","Child's Play","Alien","Scream Movies","Sinister","The Village","DeadPool","Harry Potter Movies","Piraate of the Caribbean Movies","James Bond","Puss In Boots","Legally Blond","Rocky","The Hunger Games","Godzilla","Batman","Terminator","The Hobbit","Die Hard","The Bourne Series","Tron","Frozen","Black Panther","Twilight Movies","La La Land","Get Out","The Blair Witch Project","Napoleon Dynamite","Paranormal Activities","Gravity","Gladiator","Schindler's List","The Green Mile","The Boy in Striped Pajamas","Marle y& Me","The Notebook","Requiem for a Dream","Twister","Hachi","Million Dollar Baby","Old Yeller","I Am Legend","Life is beautiful","My Girl","Karate Kid","The Elephant man","Bambi","Westside story","The Puruit of Happiness","E.T","AI","Blade Runner"]
    tv_shows = ["Six feet under","The Leftovers","Game Of thrones","Westworld","House of Dragon","Mad Men","The 100","Stranger Things","The Office","Seinfeld","The SHeild","Agents of Sheild","Marvel Series","DC Series","Justified","True Detective","House of cards","Oz","Peaky Blinder","Dark","Greenhouse Academy","Rick and Morty","The muppet show","Star Trek","Cobra Kai","The Summer I Turned Pretty","friends","Mind Hunter","Gilmore Girls","The Simpsons","Breaking Bad","The twilight Zone","Life on Mars","Only fools and heroes","Fawlty Towers","The Golden Girls","The X-Flies","Sergeant Bilko","Big Bang Theory","Young Sheldon","Modern Family","Disney Shows","Nikalodean Shows","Money Heist","The Night Agent","Bridgton","The witcher","Queen Charlotte","Money Heist","Squid Game","DAHMER","Wednesday","The Night Agent","Lucifer","Lupin","Rick and Morty","Twin Peaks"]
    breakfast = ["Breakfast Tacos","Berry Yogurt Bowl","OutMeal","Roasted POtato","Muffins","Pancakes","Waffels","Sausages","Egg Sandwitch","Smoothies","French Toast","Scrambled egg","Egg Benidect","Breakfast Bake","Breakfast Burrito","Avacodo toast","Avacodo toast with egg","Omelet","Eggs Muffins","Greek Yougert","Jams","Migas","Bruschetta","Smoothie Bowl","Flower eggs","Sunny-Side Eggs",'Shakshuka',"Granola","Overnight Chia","Hash Browns","Pancake Taco","Croque Madame","Egg Bhurji","Freanch Omlet","Cinnamon bun"]
    lunch = ["Pinwheel Sandwiches","Caesar Sandwich","Caeser salad","Burrito Bowl","Chicken Wrap","Wraps","FlatBread","Salads","Chicken Bowl","Salad Bowl","Shrimp bowls","Big Mac Crunchwrap","Fish Taco Bowl","Stuffed Pepper","Tofu Salad","Taco Salad","Pizza ","Garlic Bread","Pizza Bread","Honey Chickenn","Rice Bowls","Egg ROols Bowls","Goddess Bowl","Big Mac Salad","Fajitas","Flat Breads","Shrimp Bowls ","Falafel","Sopes","Club Sandwichs","Buddah Bowls","Quinoa Salad","Sushi","Maki","Rools","Paninis","Cabbage Wraps","Lettuce Wraps","Chilis","Pastas","spegities","Burgers","Sliders","Grains Bowls","Sandwiches","Gyros","Macaroni Salad","Chirashi Bowls","Shrimp Wraps","Veggie Sandwiches","Kimbap","Sushi Bake","Stuffed Peppers","Pie Recipes","Breadfast Bread","Soups"]
    dinner = ["Breakfast Tacos","Berry Yogurt Bowl","OutMeal","Roasted POtato","Muffins","Pancakes","Waffels","Sausages","Egg Sandwitch","Smoothies","French Toast","Scrambled egg","Egg Benidect","Breakfast Bake","Breakfast Burrito","Avacodo toast","Avacodo toast with egg","Omelet","Eggs Muffins","Greek Yougert","Jams","Migas","Bruschetta","Smoothie Bowl","Flower eggs","Sunny-Side Eggs",'Shakshuka',"Granola","Overnight Chia","Hash Browns","Pancake Taco","Croque Madame","Egg Bhurji","Freanch Omlet","Cinnamon bun""Pinwheel Sandwiches","Caesar Sandwich","Caeser salad","Burrito Bowl","Chicken Wrap","Wraps","FlatBread","Salads","Chicken Bowl","Salad Bowl","Shrimp bowls","Big Mac Crunchwrap","Fish Taco Bowl","Stuffed Pepper","Tofu Salad","Taco Salad","Pizza ","Garlic Bread","Pizza Bread","Honey Chickenn","Rice Bowls","Egg ROols Bowls","Goddess Bowl","Big Mac Salad","Fajitas","Flat Breads","Shrimp Bowls ","Falafel","Sopes","Club Sandwichs","Buddah Bowls","Quinoa Salad","Sushi","Maki","Rools","Paninis","Cabbage Wraps","Lettuce Wraps","Chilis","Pastas","spegities","Burgers","Sliders","Grains Bowls","Sandwiches","Gyros","Macaroni Salad","Chirashi Bowls","Shrimp Wraps","Veggie Sandwiches","Kimbap","Sushi Bake","Stuffed Peppers","Pie Recipes","Breadfast Bread","Soups"]
    desert = ["Cup Cakes","Muffins","Cakes","Ice  creams","Biscuits","Custards","Cookies","Pasteries","Gelatins","Pies","Puddings","Macaroons","Fruits Salads","Tarts","Brownies","Frozen Fruit Bars","Oat Apple Crisps","Yogurt Parafits","Nut Bars","Bars","Tiramisu","Angel Food Cake","Mousses","Chocolate Mousse","Fried ice cream","Strawberry Crumble","Cinnamon Cake","Cobblers","Crumbles","Puddings","Cheesecakes","s'mores","Layer cake"]
    juices = ["Apple Juice","Orange Juice","Promogranate Juices","Pineapple Juices","Amla Juices","Cranberry Juices","Watermelon Juice","Melon JUice","Carrot Juice","Avocado Juice","Cucumber","Orange and Carrot","Grape Juice","Black Grapes juice","Grape Fruit Juice","Lemonade juice","Strawberry lemon juice","Kiwi Juice","Coctail Juice","Mixed berry juice","Peach juice","Strawberry juice","Gauava Juice","Dragon Fruit Juice","Green Juice","Tomato Juice","Passion Fruit Juice"]
    mojito = ["Classic Mojito","Mojito Pitcher","Strawberry Mojito","Watermenlon Mojito","Mixed berry Mijito","Apple mojito",'Orange Mojito',"Cranbery Mojito","Carrot Mojito","Pinapple Mojito","Passion Fruit Mojito","Grape Mojito","Promogranate Mojito","Frozen Mojito","Coconut Mojito","Blueberry Mojito","Blackberry Mojito","Raseberry Mojito","Mango Mojito","Peach mojito"]
    soft_drinks = ["Fants","Miranda","Pepsi","CocaCola","Sprite","Sevenup","Lipton","Mountain Dew","Shani","Canadian Dry","Dr Peper","Ginger Ale","Grape Soda","lemon-Lid=me Soda"]
    sports = ["Foot Ball","Basket Ball","Base Ball","Soccer","Ice Hockey","Tennis","Golf","Wrestling","Car Racing","Rugby","Basminton","Feild Hockey","Cycling","Boxing","Lacrosse","VollyBall","Cricket","Track","Swiming"]
    crochet = ["Hats","Bags","Baby toys","Clothes","Plant cover or hanger","Blankets","Toys","Key Chains","Baskets","Pot Holder","Covers","Beenies","Granny Squares","Hair Scrunchies","Dish cloths","Mug Cozies","Shawls","Scarves","Coasters","Baby Flip Flops","Head Bands","Flowers","Accesories","Iphone Canes","Gloves","FInger Gloves","Cowls","Head Bands","Ear Warmers","Earings","HAir Ties","Booties","mittins","bonnets","Bibs","Loveys","Baby Items","Tank Tops","Pants","Swim Suit"]
    sewing = ["Pillow Covers","Toy Decor","Purse","Card Holder","Bed Matress","Clothing","Dress","Baby Clothes","Shirts","Pants","Bags","Reuseable sandwich Bag","Jewllery Box","Remote sleeves","Doll clothes"]


    if "time" in command:
        current_time = get_time()
        print("The current time is:", current_time)
        # Remove the word 'search' from the command and search the web using the remaining query
        query = command.replace("search", "").strip()
        search(query)
    elif "search" in command:
        # Remove the word 'search' from the command and search the web using the remaining query
        query = command.replace("search", "").strip()
        search(query)
      
    elif "note" in command:
        create_note()
        
    elif "open" in command:
        # Remove the word 'open' from the command and open the specified application or file
        target = command.replace("open", "").strip()
        try:
            subprocess.Popen(target)
            
        except FileNotFoundError:
            print("Sorry, I couldn't find the specified application or file.")
    elif "exit" in command or "quit" in command or "bye" in command:
        print("Goodbye!")
        break
    elif "hello" in command:
        print("Hi there! What can I do for you today?(type help/I need help to know more)")
    elif "help" in command or "I need help" in command:
        print("What kind of help do you need? (if you want to know what is the time just ask : what is the time, if you what to search google type (search + the thing you want to search),if you want to write a note just type (I want to write a note), if you want to know the date just type(What is the date),if you want to know the day just type(What is the day),if you want a joke just type (tell me a joke),if you want a poem just type (tell me a poem),if you to know nice short stories to read type(short stories or what short stories should i read), if you want to know what books to read just ask (books or what books shoulds i read),if you want ideas to what to draw just ask (what shoul i draw) and if you want ideas to paint (what should i paint),if you want games to play ask (what games shoud i play),if you want books for kids to read just type (kid books to read),if you what to know movies to watch (what movies should i watch)and if you wantr tv shows to watch type (what tv shos should i watch),if you want breakfast ideas ask(breakfast or what breakfast shoul i eat), and the same things for lunch and dinner (what should i eat for lunch or what should i eat for dinner), if you want ideas for desert just ask(deserts oe what shouyl i eat for desert), if you want juice ideas ask(juice or what juice shoul i drink), if you want mojitos ideas ask(mojito or what mojito shot i drink) and the same thing for soft drinks ( soft drink or what soft drinks should i drink), if you want to know what sports to play just type(sport or what sport shoul i play), if you want ideas to crochet (what should i crochet or crochet), and the same thing to sew if you was to sew just type(what should i sew or just type sew), if you want ideas of games to code tyoe(game projects), the same things for python projects or web projects or flutter project just type (python project or we project or flutter project) THANK YOU!!")
    elif "joke" in command:
      random_joke = random.choice(jokes)
      print (random_joke)
    elif "poem" in command:
        random_poem = random.choice(poems)
        print (random_poem)
    elif "short stories" in command:
        random_short_stories = random.choice(short_stories)
        print (random_short_stories)
    elif "book" in command:
        random_book = random.choice(books)
        print (random_book)
    elif "draw" in command:
        random_draw = random.choice(draw)
        print (random_draw)
    elif "paint" in command:
        random_paint = random.choice(paint)
        print (random_paint)
    elif "game project" in command:
        random_game_project = random.choice(game_projects)
        print (random_game_project)
    elif "python project" in command:
        random_python_project = random.choice(python_projects)
        print (random_python_project)
    elif "flutter project" in command:
        random_flutter_project = random.choice(flutter_projects)
        print (random_flutter_project)
    elif "web project" in command:
        random_web_project = random.choice(web_projects)
        print (random_web_project)
    elif "business" in command:
        random_business = random.choice(business_ideas)
        print (random_business)
    elif "kid book" in command:
        random_kid_book = random.choice(kid_books)
        print (random_kid_book)
    elif "games" in command:
        random_games = random.choice(games)
        print (random_games)
    elif "movie" in command:
       random_movie = random.choice(movies)
       print (random_movie)
    elif "tv show" in command:
        random_tv_show = random.choice(tv_shows)
        print (random_tv_show)
    elif "breakfast" in command:
        random_breakfast = random.choice(breakfast)
        print (random_breakfast)
    elif "lunch" in command:
        random_lunch = random.choice(lunch)
        print (random_lunch)
    elif "dinner" in command:
        random_dinner = random.choice(dinner)
        print (random_dinner)
    elif "desert" in command:
        random_desert = random.choice(desert)
        print (random_desert)
    elif "juice" in command:
        random_juice = random.choice(juices)
        print (random_juice)
    elif "mojito" in command:
        random_mojito = random.choice(mojito)
        print (random_mojito)
    elif "soft drink" in command:
        random_soft_drink = random.choice(soft_drinks)
        print (random_soft_drink)
    elif "sport" in command:
        random_sport = random.choice(sports)
        print (random_sport)
    elif "crochet" in command:
        random_crochet = random.choice(crochet)
        print (random_crochet)
    elif "sew" in command:
        random_sew = random.choice(sewing)
        print (random_sew)
    else:
        print("Sorry, I couldn't understand. Can you please repeat?")
