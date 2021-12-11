import discord
import asyncio
import random
from datetime import datetime

client = discord.Client()
#The block below opens the totals.txt ( file, reads the first line, and stores whats in it in the toConvert Variable
#it then converts that string it read into an integer so we can do arithmetic with it.
totalFile = open("totals.txt",'r')
toConvert = totalFile.read()
totalPaid = int(toConvert)
#The block below opens up the saved total file, stores the first line in toInt, then count converts the string to an int so we
#can do arithmetic with it. SavedTotal.txt stores the total amount paid to the commission.
f = open("savedTotal.txt",'r')
toInt =f.read()
count = int(toInt)

#this block opens cleanTotal.txt, stores the first line as a string in toClean, then its converted to an int and stored in cleanCount.
#clean total stores the amount of money the gang has that's clean.
clean = open("cleanTotal.txt",'r')
toClean = clean.read()
cleanCount=int(toClean)
print(cleanCount)


msgAuthor = ""
msgContent = "" #recieves msg.content from the if statement in !add or !subtract (Eg: 10, 20, 200)
messageContent = "" #receieves message.content from players command input (Eg: !add !subtract etc)
firstMSG = ""

colors = [1752220, 3066993, 3447003, 10181046, 15844367,
          15105570, 15158332, 9807270, 8359053, 3426654,
          1146986, 2067276, 16580705, 12320855, 9936031,
          2123412, 7419530]

def timestamp():
    now = datetime.now()
    dt = now.strftime("%m/%d/%Y %H:%M:%S")
    return dt

def commandsListEmbed():
    commandsListEmbed = discord.Embed(title="TheFirmBot", description="Version 1.2", color=random.choice(colors),inline=True)
    commandsListEmbed.add_field(name="Commands:",value = "----->")
    commandsListEmbed.add_field(name="!clean add", value="Add to the CLEAN money balance.", inline=True)
    commandsListEmbed.add_field(name="!clean subtract", value="Subtract from the CLEAN money balance.", inline=True)
    commandsListEmbed.add_field(name="!clean balance", value="View the CLEAN money balance.", inline=True)
    commandsListEmbed.add_field(name="!dirty balance", value="View the DIRTY money balance.",inline=True)
    commandsListEmbed.add_field(name="!dirty add", value="Adds to the DIRTY money balance. ",inline=True)
    commandsListEmbed.add_field(name='!dirty subtract', value='Subtract from the DIRTY money balance..',inline=True)
    commandsListEmbed.add_field(name='!set dirty balance', value='Sets the dirty money total.',inline=True)
    commandsListEmbed.add_field(name="!set commission total", value="Set the total paid to the commission.",inline=True)
    commandsListEmbed.add_field(name='!commission total', value="Displays the total paid to the commission so far.",inline=True)
    commandsListEmbed.add_field(name='!commission add', value="Add to the total amount paid to the commission.",inline=True)
    commandsListEmbed.add_field(name='!commission subtract', value="Subtract a number to the commission payment total.",inline=True)
    commandsListEmbed.add_field(name='!logs', value="The bot will post the current log files so you can download them.",inline=True)
    commandsListEmbed.add_field(name='!ip', value="The bot will post the server IP so you can quickly connect.",inline=True)
    commandsListEmbed.set_footer(text="Made by Natsukvshii#0417 (Mike)")
    return commandsListEmbed

def additionDirtyEmbed():
    additionEmbed = discord.Embed(title="How much would you like to ADD to the dirty money balance? (" + str(count) + ")",description="||This request will time out in 45 seconds\n If no answer is received.||",color=15158332)
    additionEmbed.add_field(name="How to:", value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")

    return additionEmbed

def additionCleanEmbed():
    additionEmbed = discord.Embed(title="How much would you like to ADD to the CLEAN money balance? (" + str(cleanCount) + ")",description="||This request will time out in 45 seconds\n If no answer is received.||",color=3066993)
    additionEmbed.add_field(name="How to:", value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")

    return additionEmbed

def commissionAddEmbed():
    toFix = open("totals.txt", 'r')
    fixed = toFix.read()
    additionEmbed = discord.Embed(
        title="How much would you like to ADD to the total paid to the commission? (" + str(fixed) + ")", description="||This request will time out in 45 seconds\n If no answer is received.||",color=random.choice(colors))
    additionEmbed.add_field(name="How to:", value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")
    return additionEmbed

def subtractionDirtyEmbed():
    myEmbed = discord.Embed(title="How much would you like to SUBTRACT from the dirty money balance? (" + str(count) + ")",description="||This request will time out in 45 seconds\n If no answer is received.||",color=15158332)
    myEmbed.add_field(name="How to:",value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")
    return myEmbed

def subtractionCleanEmbed():
    myEmbed = discord.Embed(title="How much would you like to SUBTRACT from the CLEAN money balance? (" + str(cleanCount) + ")",description="||This request will time out in 45 seconds\n If no answer is received.||",color=3066993)
    myEmbed.add_field(name="How to:",value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")
    return myEmbed

def totalPaidToCommissionEmbed():
    setTotalPaidEmbed = discord.Embed(title="Set the amount paid to commission this month.",color=random.choice(colors))
    setTotalPaidEmbed.add_field(name="How to:",value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")
    return setTotalPaidEmbed

def newDirtyBalance():
    totalEmbed = discord.Embed(title="New balance is:", description="$" + "{:,}".format(count),color=15158332)
    return totalEmbed

def newCleanBalance():
    totalEmbed = discord.Embed(title="New clean balance is:", description="$" + "{:,}".format(cleanCount),
                               color=3066993)
    return totalEmbed

def newCommissionPaymentTotal():
    totalEmbed = discord.Embed(title="New total payments amount to:", description="$" + "{:,}".format(totalPaid),color=random.choice(colors))
    return totalEmbed


def setBalanceEmbed():
    setBalanceEmbed = discord.Embed(title="What do you want to SET the DIRTY money balance to?",description="||This request will time out in 45 seconds\n If no answer is received.||", color=15158332)
    setBalanceEmbed.add_field(name="How to:", value="Please don't respond to this message with any alphabetical characters, only numbers.\n EX: $2,000,000 or 2,000,000 or 2000000 are all valid. 'Two million' is not lol ")
    return setBalanceEmbed

def newCommission():
    totalEmbed = discord.Embed(title="New Commission Total:", description="$" + "{:,}".format(totalPaid),color=random.choice(colors))
    return totalEmbed

def dirtyBalanceEmbed():
    totalEmbed = discord.Embed(title="Total DIRTY Money Balance:", description="$" + "{:,}".format(count),color=15158332)
    return totalEmbed

def cleanBalanceEmbed():
    totalEmbed = discord.Embed(title="Total CLEAN Money Balance:", description="$" + "{:,}".format(cleanCount),color=3066993)
    return totalEmbed

def saveDirtyBalance():
    f = open("savedTotal.txt", 'w')
    f.write(str(count))
    f.close()

def saveCleanBalance():
    f = open("cleanTotal.txt",'w')
    f.write(str(cleanCount))
    f.close()

def saveCommissionTotal():
    f = open('totals.txt', 'w')
    f.write(str(totalPaid))
    f.close()

def logDirtyBalance():
    f = open('log.txt','a')
    string = str(msgAuthor) + " used: |"+str(messageContent)+"| "+"Amount: $ "+msgContent+" New Total: $"+str(count)+" Date:"+str(timestamp()+"\n")
    f.write(string)
    f.close()

def logCleanBalance():
    f = open('log.txt','a')
    string = str(msgAuthor) + " used: |" + str(
        messageContent) + "| " + "Amount: $ " + msgContent + " New Total: $" + str(cleanCount) + " Date:" + str(
        timestamp() + "\n")
    f.write(string)
    f.close()

def logCommission():
    f = open('CommissionLogs.txt','a')
    string = str(msgAuthor) + " used: |" + str(messageContent) + "| " + "Amount: $ " + msgContent + " New Total: $" + str(totalPaid) + " Date:" + str(timestamp() + "\n")
    f.write(string)
    f.close()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!firm commands'))

    print("Logged in as: " + client.user.name)
    print("Client User ID: " + str(client.user.id))
    print('---------------------------')

@client.event
async def on_message(message):
    global count,totalPaid,msgAuthor,msgContent, firstMSG,messageContent, cleanCount

    colors = [1752220, 3447003, 10181046, 15844367,
              15105570, 9807270, 8359053, 3426654,
              1146986, 2067276, 16580705, 12320855, 9936031,
              2123412, 7419530]

    if message.content.lower() == '!firm commands':
        print(message.author, "used:", "|",message.content,"|", "Date:",timestamp() )
        return await message.channel.send(embed = commandsListEmbed())

    elif message.content.lower() == "!commission add":
        sent = await message.channel.send(embed = commissionAddEmbed())
        try:
            msg = await client.wait_for("message", timeout = 45, check=None)
            if msg:
                msg.content = msg.content.replace(",","").replace("$","")
                totalPaid += int(float(msg.content))

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                saveCommissionTotal()
                logCommission()
                string = str(msgAuthor) + " used: |" + str(messageContent) + "| " + "Amount: $ " + msgContent + " New Total: $" + str(totalPaid) + " Date:" + str(timestamp())
                print(string)
                await message.channel.send(embed=newCommissionPaymentTotal())
        except asyncio.TimeoutError:
            await sent.delete()
            await message.channel.send("Sorry, request timed out!")

    elif message.content.lower() == "!commission subtract":
        #sent = await message.channel.send(embed=commissionAddEmbed())
        sent = await message.channel.send(embed=commissionAddEmbed())
        try:
            msg = await client.wait_for("message", timeout=45, check=None)
            if msg:
                msg.content = msg.content.replace(",", "").replace("$", "")
                totalPaid -= int(float(msg.content))

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                saveCommissionTotal()
                logCommission()
                string = str(msgAuthor) + " used: |" + str(messageContent) + "| " + "Amount: $ " + msgContent + " New Total: $" + str(totalPaid) + " Date:" + str(timestamp())
                print(string)
                await message.channel.send(embed=newCommissionPaymentTotal())
        except asyncio.TimeoutError:
            await sent.delete()
            await message.channel.send("Sorry, request timed out!")


    elif message.content.lower() == "!dirty add":
        sent = await message.channel.send(embed = additionDirtyEmbed())
        try:
            msg = await client.wait_for("message",timeout=45, check=None)
            if msg:
                msg.content = msg.content.replace(",","")
                msg.content = msg.content.replace("$","")
                count += int(float(msg.content))
                saveDirtyBalance()

                await message.channel.send(embed=newDirtyBalance())

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                print(message.author, "used:","|",message.content,"|","Amount: $",msgContent, "New Total: $",count, "Date:",timestamp())
                logDirtyBalance()
        except asyncio.TimeoutError:
            await sent.delete()
            await message.channel.send("Sorry, request timed out!")

    elif message.content.lower() == "!clean add":
        sent = await message.channel.send(embed = additionCleanEmbed())
        try:
            msg = await client.wait_for("message",timeout=45, check=None)
            if msg:
                msg.content = msg.content.replace(",","")
                msg.content = msg.content.replace("$","")
                cleanCount += int(float(msg.content))
                saveCleanBalance()

                await message.channel.send(embed=newCleanBalance())

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                print(message.author, "used:","|",message.content,"|","Amount: $",msgContent, "New Total: $",cleanCount, "Date:",timestamp())
                logCleanBalance()
        except asyncio.TimeoutError:
            await sent.delete()
            await message.channel.send("Sorry, request timed out!")

    elif message.content.lower() == "!clean subtract":
        sent = await message.channel.send(embed = subtractionCleanEmbed())
        try:
            msg = await client.wait_for("message",timeout=45, check=None)
            if msg:
                msg.content = msg.content.replace(",","")
                msg.content = msg.content.replace("$","")
                cleanCount -= int(float(msg.content))
                saveCleanBalance()

                await message.channel.send(embed=newCleanBalance())

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                print(message.author, "used:","|",message.content,"|","Amount: $",msgContent, "New Total: $",cleanCount, "Date:",timestamp())
                logCleanBalance()
        except asyncio.TimeoutError:
            await sent.delete()
            await message.channel.send("Sorry, request timed out!")

    elif message.content.lower() == "!dirty subtract":
        sent = await message.channel.send(embed=subtractionDirtyEmbed())
        try:
            msg = await client.wait_for("message", timeout=45, check=None)
            if msg:
                msg.content = msg.content.replace(",", "")
                msg.content = msg.content.replace("$", "")

                count -= int(msg.content)
                saveDirtyBalance()
                print(message.author, "used:","|",message.content,"|", "Amount: $", str(msg.content), "New Total: $",count, "Date:", timestamp())
                await message.channel.send(embed=newDirtyBalance())

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content
                logDirtyBalance()
        except asyncio.TimeoutError:
            await sent.delete()
            await message.channel.send("Sorry, you took too long!")

    elif message.content.lower() == "!dirty balance":
        print(message.author, "used:", message.content, "Date:", datetime.now())
        await message.channel.send(embed=dirtyBalanceEmbed())

    elif message.content.lower() == "!clean balance":
        print(message.author, "used:", message.content, "Date:", datetime.now())
        await message.channel.send(embed=cleanBalanceEmbed())

    elif message.content.lower() == "!set dirty balance":
        await message.channel.send(embed = setBalanceEmbed())
        try:
            msg = await client.wait_for("message", timeout=45, check=None)

            if msg:
                msg.content = msg.content.replace(",", "")
                msg.content = msg.content.replace("$", "")
                count = int(msg.content)
                saveDirtyBalance()

                await message.channel.send(embed=newDirtyBalance())

                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                logDirtyBalance()
                print(message.author, "used:", "|", message.content, "|", "Amount: $", str(msg.content), "New Total: $",str(count), "Date:", timestamp())

        except asyncio.TimeoutError:
            await message.channel.send("Sorry, you took too long!")

    elif message.content.lower() == "!set commission total":

        await message.channel.send(embed = totalPaidToCommissionEmbed())
        try:
            msg = await client.wait_for("message", timeout=45, check=None)
            if msg:
                msg.content = msg.content.replace(",", "")
                msg.content = msg.content.replace("$", "")
                #below is used to convert data types so the logCommission(), saveCommissionTotal() functions actually work
                totalPaid = int(msg.content)
                msgAuthor = message.author
                msgContent = str(msg.content)
                messageContent = message.content

                logCommission()
                saveCommissionTotal()
                print(message.author, "used:", "|", message.content, "|", "Amount: $", str(msg.content), "New Total: $",totalPaid, "Date:", timestamp())
            await message.channel.send(embed=newCommission())
        except asyncio.TimeoutError:
            await message.channel.send("Sorry, you took too long!")

    elif message.content.lower() == "!commission total":
        toFix = open("totals.txt",'r')
        fixed = toFix.read()
        print(message.author, "used:", message.content, "Date:", timestamp())
        totalEmbed = discord.Embed(title="Total Paid to The Commission:", description="$"+ "{:,}".format(int(fixed)), color=random.choice(colors))
        sent = await message.channel.send(embed=totalEmbed)
        emojis = ['🇳','🇮','🇨','🇪']
        for emoji in emojis:
            await sent.add_reaction(emoji)

    elif message.content.lower() == "!logs":
        await message.delete()
        await message.channel.send("Here are your log files:\n||These messages will self destruct after 30 seconds.||", delete_after = 30)
        with open("CommissionLogs.txt", "rb") as file:
            await message.channel.send(file=discord.File(file, 'CommissionLogs.txt'),delete_after = 30 )
        with open("log.txt","rb") as file2:
            await message.channel.send(file = discord.File(file2, 'log.txt'), delete_after = 30)
        print(mesage.author, "Asked for the logs.", timestamp())

    elif message.content.lower() == "!ip":
        await message.delete()
        await message.channel.send("```connect SERVER IP GOES HERE```", delete_after = 30)
        print(message.author, "Asked for the IP Date:", timestamp())




client.run('API KEY GOES HERE')