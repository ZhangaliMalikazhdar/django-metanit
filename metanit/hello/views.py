from .models import Person
import asyncio


async def abulk_person():
    people = await Person.objects.abulk_create([
        Person(name='AKate', age=33),
        Person(name='ARose', age=45),
    ])

asyncio.run(abulk_person())

