


@router_stat.message(Command("start"))
async def start(msg: Message):

    if await find_value_in_csv(str(msg.from_user.id)):
        await msg.answer_animation(Data.file_wakeUP, caption="Вкл", reply_markup=kb.admin_key)
    else:
        await msg.answer("""Мы можем беседовать часами, но на самом деле я только дожидаюсь, когда ты напишешь 'хорошо, что мы закончили'""")
        await msg.answer_animation(Data.file_start)