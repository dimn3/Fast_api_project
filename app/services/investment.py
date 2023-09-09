import datetime
from typing import List

from sqlalchemy import select

from app.models import CharityProject, Donation


async def check_is_not_full_amount(model, session) -> List:
    investments = await session.execute(
        select(model).where(
            model.fully_invested == False  # noqa: E712
        )
    )
    return investments.scalars().all()

@staticmethod
def transfer(transfer_first, transfer_second, session):
    transfer_first.invested_amount += (
        transfer_second.full_amount - transfer_second.invested_amount
    )
    transfer_second.invested_amount = transfer_second.full_amount
    transfer_second.fully_invested = True
    transfer_second.close_date = datetime.datetime.utcnow()
    if transfer_first.full_amount == transfer_first.invested_amount:
        transfer_first.fully_invested = True
        transfer_first.close_date = datetime.datetime.utcnow()
    


async def transfer_invested_amount_lt(
        transfer_to, transfer_from, session
):
    transfer(
        transfer_first=transfer_to,
        transfer_second=transfer_from,
        session=session
    )
    session.add(transfer_to)
    session.add(transfer_from)
    await session.commit()
    await session.refresh(transfer_to)
    return transfer_to


async def transfer_invested_amount_gt(
        transfer_to, transfer_from, session
):
    transfer(
        transfer_first=transfer_from,
        transfer_second=transfer_to,
        session=session
    )
    session.add(transfer_to)
    session.add(transfer_from)
    await session.commit()
    await session.refresh(transfer_to)
    return transfer_to


async def investment(new_object, session):
    if isinstance(new_object, CharityProject):
        model = Donation
    else:
        model = CharityProject

    investments = await check_is_not_full_amount(model, session)
    result = []
    if not investments:
        return
    more_to_invest = (
        investments[0].full_amount - investments[0].invested_amount
    )
    for investment_obj in investments:
        if new_object.fully_invested:
            if new_object.full_amount == new_object.invested_amount:
                break

        await session.refresh(investment_obj)
        await session.refresh(new_object)

        if new_object.full_amount < more_to_invest:
            added_amount = await transfer_invested_amount_gt(
                new_object,
                investment_obj,
                session
            )
            result.append(added_amount.invested_amount)
            await session.refresh(investment_obj)
            more_to_invest = (
                investment_obj.full_amount - investment_obj.invested_amount
            )

        else:
            added_amount = await transfer_invested_amount_lt(
                new_object,
                investment_obj,
                session
            )
            result.append(added_amount.invested_amount)
            await session.refresh(investment_obj)
            more_to_invest = (
                investment_obj.full_amount - investment_obj.invested_amount
            )
