from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

sv = Service('chara-voice', manage_priv=Priv.ADMIN, visible=True)

from .ub_voice import *
