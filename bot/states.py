from aiogram.fsm.state import State, StatesGroup


class MBTITest(StatesGroup):
    answering = State()


class IQTest(StatesGroup):
    answering = State()


class EQTest(StatesGroup):
    answering = State()
