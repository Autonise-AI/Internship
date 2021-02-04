import asyncio

async def heighest_number_below(n):
    print(f'number : {n}')
    for x in range(1,n):
        await asyncio.sleep(0.001)

    print(f"for {n} the ans is: {x}")


async def main():

    n1= 2000
    n2= 1000
    n3= 100
    await asyncio.wait([
        heighest_number_below(n1),
        heighest_number_below(n2),
        heighest_number_below(n3)
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

    
