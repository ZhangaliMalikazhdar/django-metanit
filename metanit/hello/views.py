from .models import Person
import asyncio


async def get_person():
    person = await Person.objects.aget(id=1)
    print(person.name)

asyncio.run(get_person())
