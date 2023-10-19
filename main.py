import random
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.command(name='rps', aliases=['rockpaperscissors'])
async def rps(ctx, user_choice):
    choices = ['камень', 'бумага', 'ножницы']
    bot_choice = random.choice(choices)
    user_choice = user_choice.lower()

    if bot_choice == user_choice:
        await ctx.send(f'Это была ничья! {bot_choice}')
    elif bot_choice == 'камень' and user_choice == 'бумага':
        await ctx.send(f'Вы выбрали ** {user_choice}**!, Я выбрал **{bot_choice}**!\nТы выиграл!')
    elif bot_choice == 'камень' and user_choice == 'ножницы':
        await ctx.send(f'Вы выбрали ** {user_choice}**!, Я выбрал **{bot_choice}**!\nЯ выиграл!')
    elif bot_choice == 'бумага' and user_choice == 'камень':
        await ctx.send(f'Вы выбрали ** {user_choice}**!, Я выбрал **{bot_choice}**!\nЯ выиграл!')
    elif bot_choice == 'бумага' and user_choice == 'ножницы':
        await ctx.send(f'Вы выбрали ** {user_choice}**!, Я выбрал **{bot_choice}**!\nТы выиграл!')
    elif bot_choice == 'ножницы' and user_choice == 'бумага':
        await ctx.send(f'Вы выбрали ** {user_choice}**!, Я выбрал **{bot_choice}**!\nЯ выиграл!')
    elif bot_choice == 'ножницы' and user_choice == 'камень':
        await ctx.send(f'Вы выбрали ** {user_choice}**!, Я выбрал **{bot_choice}**!\nТы выиграл!')
    else:
        await ctx.send(
            f"Извините, но, похоже, возникла проблема при выполнении команды! Пожалуйста, убедитесь, что вы выбрали один из следующих вариантов.\n`{choices[0]}`, `{choices[1]}`, `{choices[2]}`")


@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please make sure you put your choice in the message.\nchoices : `камень`, `бумага`, `ножницы`')


client.run('ID Botaaaaa....')
