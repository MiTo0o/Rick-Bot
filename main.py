import discord
import os
from datetime import datetime, timedelta
import praw
from discord.ext import commands
import random
from stay_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '$')
client.remove_command("help")
spams = {}

reddit = praw.Reddit(client_id = "KWWOg-CxVx_DCw",
                     client_secret = os.getenv("REDDIT_SECRECT"),
                     username = "NightTime-BabyLotion",
                     password =os.getenv("REDDIT_PASS"),
                     user_agent = "praw_boi"
                     )

copy_pasta = 'Whenever I get a package of plain M&Ms, I make it my duty to continue the strength and robustness of the candy as a species. To this end, I hold M&M duels. Taking two candies between my thumb and forefinger, I apply pressure, squeezing them together until one of them cracks and splinters. That is the “loser,” and I eat the inferior one immediately. The winner gets to go another round. I have found that, in general, the brown and red M&Ms are tougher, and the newer blue ones are genetically inferior. I have hypothesized that the blue M&Ms as a race cannot survive long in the intense theater of competition that is the modern candy and snack-food world. Occasionally I will get a mutation, a candy that is misshapen, or pointier, or flatter than the rest. Almost invariably this proves to be a weakness, but on very rare occasions it gives the candy extra strength. In this way, the species continues to adapt to its environment. When I reach the end of the pack, I am left with one M&M, the strongest of the herd. Since it would make no sense to eat this one as well, I pack it neatly in an envelope and send it to M&M Mars, A Division of Mars, Inc., Hackettstown, NJ 17840-1503 U.S.A., along with a 3×5 card reading, “Please use this M&M for breeding purposes.” This week they wrote back to thank me, and sent me a coupon for a free 1/2 pound bag of plain M&Ms. I consider this “grant money.” I have set aside the weekend for a grand tournament. From a field of hundreds, we will discover the True Champion. There can be only one.'

@client.event
async def on_ready():
    print("ya boi {0.user} is ready.".format(client))

@client.command(aliases=['c'])
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['dm'])
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "Rick is reminding you to hydrate."
    await user.send(message)

# @client.event
# async def on_message(message):
#     global spams
#     if message.author == client.user:
#         return
#     if '$DM_spam' in message.content or '$dm_spam' in message.content or '$dmspam' in message.content or '$dmSpam' in message.content or '$spam' in message.content:
#         if message.author not in spams:
#             spams[message.author] = [datetime.now()]
#         else:
#             now = datetime.now()
#             spams[message.author] = [t for t in spams[message.author] if now - t < timedelta(minutes = 1)]
#             spams[message.author].append(now)
#     print(spams)


@client.command(aliases=['dm_spam','dmspam','dmSpam'])
async def DM_spam(ctx, user: discord.User, amount = 10, *, message=None):
    # global spams
    # author = ctx.message.author
#         if message.author not in spams:
#             spams[message.author] = [datetime.now()]
#         else:
#             now = datetime.now()
#             spams[message.author] = [t for t in spams[message.author] if now - t < timedelta(minutes = 1)]
#             spams[message.author].append(now)
    # if len(spams[author]) >= 3:
    #     await ctx.send("shut up")
    #     return
    message = message or copy_pasta
    if amount > 10:
        amount = 10
    for i in range(amount):
        await user.send(message)

@client.command()
async def spam(ctx, amount = 10, *, message = None):
    # global spams
    # author = ctx.message.author
#         if message.author not in spams:
#             spams[message.author] = [datetime.now()]
#         else:
#             now = datetime.now()
#             spams[message.author] = [t for t in spams[message.author] if now - t < timedelta(minutes = 1)]
#             spams[message.author].append(now)
    # print(author)
    # if len(spams[author]) >= 3:
    #     await ctx.send("shut up")
    #     return
    message = message or copy_pasta
    if amount > 10:
        amount = 10
    for i in range(amount):
        await ctx.send(message)

@client.command(aliases=['h'])
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        description="U need some help?",
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Help Panel")
    embed.set_image(url= "https://memegenerator.net/img/instances/39456992/you-need-help.jpg")
    embed.set_thumbnail(url="https://sayingimages.com/wp-content/uploads/stop-it-help-meme.jpg")
    embed.add_field(name="$help", value="shows you all the commands", inline=False)
    embed.add_field(name="$DM", value="DMs a member of the server ($DM @user message)", inline=False)
    embed.add_field(name="$little_boi", value="lists a user as a little boi ($little_boi @user)", inline=False)
    embed.add_field(name="$clear", value="clears message ($clear lines)", inline=False)
    embed.add_field(name="$meme", value="gives random top rated meme from a random meme subreddit\n(memes, dankmemes, ProgrammerHumor, animememes)", inline=False)
    embed.add_field(name="$surprise", value="surprises you", inline=False)
    embed.add_field(name="$DM_spam", value="spams the dm of a user($DM_spam @user amount content)", inline=False)
    embed.add_field(name="$spam", value="spams the chat($spam amount content)", inline=False)
    embed.add_field(name="$8ball", value="reveals an answer to a yes-no question", inline=False)

    await author.send(embed=embed)

@client.command()
async def meme(ctx):
    # "dankmemes", "nukememes", "surrealmemes", "bigbangedmemes", "animememes",
    s_list = ['memes', 'dankmemes', 'ProgrammerHumor', 'animememes']
    s_reddit = random.choice(s_list)
    subreddit = reddit.subreddit(s_reddit).top(limit=30)
    all_top_posts = []

    for post in subreddit:
        all_top_posts.append(post)
    rand_post = random.choice(all_top_posts)
    name = rand_post.title
    url = rand_post.url

    embed = discord.Embed(
        title=name
    )
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@client.command(aliases=['l_boi', 'lil_boi',])
async def little_boi(ctx, user: discord.User):

    embed = discord.Embed(
        title = "Little Boi",
        colour = discord.Colour.blue()
    )
    embed.add_field(name=f"{user.name} is a little boi.", value="Puny\nSmall\nTiny\nMini\nMicroscopic\nShrimp\nMeasly", inline=False)
    embed.set_thumbnail(url= user.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases = ['8ball','eight_ball', 'eightBall', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don’t count on it',
                'It is certain',
                'It is decidedly so'
                'Most likely',
                'My reply is no',
                'My sources say no',
                'Outlook good',
                'Outlook not so good',
                'Reply hazy try again',
                'Signs point to yes',
                'Very doubtful',
                'Without a doubt',
                'Yes',
                'Yes, definitely',
                'You may rely on it']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def surprise(ctx):
    author = ctx.message.author
    r1 = "https://www.youtube.com/watch?v=HPk-VhRjNI8&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=1"
    r2 = "https://www.youtube.com/watch?v=Uj1ykZWtPYI&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=2"
    r3 = "https://www.youtube.com/watch?v=EE-xtCF3T94&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=3"
    r4 = "https://www.youtube.com/watch?v=V-_O7nl0Ii0&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=4"
    r5 = "https://www.youtube.com/watch?v=vkbQmH5MPME&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=5"
    r6 = "https://www.youtube.com/watch?v=ikFZLI4HLpQ&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=7"
    r7 = "https://www.youtube.com/watch?v=0SoNH07Slj0&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=8"
    r8 = "https://www.youtube.com/watch?v=xfr64zoBTAQ&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=9"
    r9 = "https://www.youtube.com/watch?v=cqF6M25kqq4&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=10"
    r10 = "https://www.youtube.com/watch?v=j5a0jTc9S10&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=11"
    r11 = "https://www.youtube.com/watch?v=dPmZqsQNzGA&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=12"
    r12 = "https://www.youtube.com/watch?v=ID_L0aGI9bg&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=13"
    r13 = "https://www.youtube.com/watch?v=nHRbZW097Uk&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=15"
    rick_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13]
    random_rick = random.choice(rick_list)
    await ctx.send(random_rick)
    await author.send(random_rick)
    
keep_alive()
client.run(os.getenv("TOKEN"))

