# Copyright (C) 2020 - 2021 Divkix. All rights reserved. Source code available under the AGPL.
#
# This file is part of Alita_Robot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


RUN_STRINGS = (
    "Huh? what? did they get away?",
    "Get back here!",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You've got company!",
    "Chotto matte!",
    "Yare yare daze",
    "Hey take responsibilty for what you just did!",
    "May the odds be ever in your favour.",
    "Run everyone, they just dropped a bomb 💣💣",
    "And they disappeared forever, never to be seen again.",
    "Legend has it, they're still running.",
    "Hasta la vista, baby.",
    "Ah, what a waste. I liked that one.",
    "As The Doctor would say... RUN!",
)


SLAP_ALITA_TEMPLATES = (
    "Slap me one more time and I'll mute you.",
    "Don't again dare to slap me asshole.",
)


SLAP_TEMPLATES = (
    "{user2} was shot by {user1}.",
    "{user2} walked into a cactus while trying to escape {user1}.",
    "{user2} drowned whilst trying to escape {user1}.",
    "{user2} fell into a patch of cacti.",
    "{user2} went up in flames.",
    "{user2} burned to death.",
    "{user2} was burnt to a crisp whilst fighting {user1}.",
    "{user2} was struck by lightning.",
    "{user2} was slain by {user1}.",
    "{user2} was killed by magic.",
    "{user2} starved to death.",
    "{user2} fell out of the world.",
    "{user2} was knocked into the void by {user1}.",
    "{user2}'s bones are scraped clean by the desolate wind.",
    "{user2} fainted.",
    "{user2} is out of usable Pokemon! {user2} whited out!.",
    "{user2} is out of usable Pokemon! {user2} blacked out!.",
    "{user2} says goodbye to this cruel world.",
    "{user2} got rekt.",
    "{user2} was sawn in half by {user1}.",
    "{user2}'s melon was split by {user1}.",
    "{user2} was sliced and diced by {user1}.",
    "{user2}'s death put another notch in {user1}'s axe.",
    "{user2} died from {user1}'s mysterious tropical disease.",
    "{user2} played hot-potato with a grenade.",
    "{user2} was knifed by {user1}.",
    "{user2} ate a grenade.",
    "{user2} is what's for dinner!",
    "{user2} was terminated by {user1}.",
    "{user2} was shot before being thrown out of a plane.",
    "{user2} has encountered an error.",
    "{user2} died and reincarnated as a goat.",
    "{user1} threw {user2} off a building.",
    "{user2} got a premature burial.",
    "{user1} spammed {user2}'s email.",
    "{user1} hit {user2} with a small, interstellar spaceship.",
    "{user1} put {user2} in check-mate.",
    "{user1} RSA-encrypted {user2} and deleted the private key.",
    "{user1} put {user2} in the friendzone.",
    "{user1} slaps {user2} with a DMCA takedown request!",
    "{user2} died of hospital gangrene.",
    "{user2} got a house call from Doctor {user1}.",
    "{user1} beheaded {user2}.",
    "{user2} got stoned...by an angry mob.",
    "{user1} sued the pants off {user2}.",
    "{user2} was one-hit KO'd by {user1}.",
    "{user1} sent {user2} down the memory hole.",
    "{user2} was a mistake. - '{user1}' ",
    "{user1} checkmated {user2} in two moves.",
    "{user2} was made redundant.",
    "{user1} {hits} {user2} with a bat!.",
    "{user1} {hits} {user2} with a Taijutsu Kick!.",
    "{user1} {hits} {user2} with X-Gloves!.",
    "{user1} {hits} {user2} with a Jet Punch!.",
    "{user1} {hits} {user2} with a Jet Pistol!.",
    "{user1} {hits} {user2} with a United States of Smash!.",
    "{user1} {hits} {user2} with a Detroit Smash!.",
    "{user1} {hits} {user2} with a Texas Smash!.",
    "{user1} {hits} {user2} with a California Smash!.",
    "{user1} {hits} {user2} with a New Hampshire Smash!.",
    "{user1} {hits} {user2} with a Missouri Smash!.",
    "{user1} {hits} {user2} with a Carolina Smash!.",
    "{user1} {hits} {user2} with a King Kong Gun!.",
    "{user1} {hits} {user2} with a baseball bat - metal one.!.",
    "*Serious punches {user2}*.",
    "*Normal punches {user2}*.",
    "*Consecutive Normal punches {user2}*.",
    "*Two Handed Consecutive Normal Punches {user2}*.",
    "*Ignores {user2} to let them die of embarassment*.",
    "*points at {user2}* What's with this sassy... lost child?.",
    "*Hits {user2} with a Fire Tornado*.",
    "{user1} pokes {user2} in the eye !",
    "{user1} pokes {user2} on the sides!",
    "{user1} pokes {user2}!",
    "{user1} pokes {user2} with a needle!",
    "{user1} pokes {user2} with a pen!",
    "{user1} pokes {user2} with a stun gun!",
    "{user2} is secretly a Furry!.",
    "Hey Everybody! {user1} is asking me to be mean!",
    "( ･_･)ﾉ⌒●~* (･.･;) <-{user2}",
    "Take this {user2}\n(ﾉﾟДﾟ)ﾉ ))))●~* ",
    "Here {user2} hold this\n(｀・ω・)つ ●~＊",
    "( ・_・)ノΞ●~*  {user2}\nDieeeee!!.",
    "( ・∀・)ｒ鹵~<≪巛;ﾟДﾟ)ﾉ\n*Bug sprays {user2}*.",
    "( ﾟДﾟ)ﾉ占~<巛巛巛.\n-{user2} You pest!",
    r"( う-´)づ︻╦̵̵̿╤── \(˚☐˚”)/ {user2}.",
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava.",
    "{user1} bullied {user2}.",
    "Nyaan ate {user2}'s leg. *nomnomnom*",
    "{user1} {throws} a master ball at {user2}, resistance is futile.",
    "{user1} hits {user2} with an action beam...bbbbbb (ง・ω・)ง ====*",
    "{user1} ara ara's {user2}.",
    "{user1} ora ora's {user2}.",
    "{user1} muda muda's {user2}.",
    "{user2} was turned into a Jojo reference!",
    "{user1} hits {user2} with {item}.",
    "Round 2!..Ready? .. FIGHT!!",
    "WhoPixel will oof {user2}, to infinity and beyond."
    "{user2} ate a bat and discovered a new disease.",
    "{user1} folded {user2} into a paper plane",
    "{user1} exchanged {user2}'s life-force for a cup of chocolate.",
    "{user2} did a 69 with a cactus.",
    "{user1} served {user2} some bat soup.",
    "{user2} was sent to his home, the planet of apes.",
    "{user1} kicked {user2} out of a moving train.",
    "{user1} traveled to the future and spat on {user2}'s grave.",
    "{user2} died from talk-no-jutsu.",
    "{user2} was placed as a carpet for a stomp dance competition.",
    "{user2} just killed John Wick’s dog.",
    "{user1} performed an Avada Kedavra spell on {user2}.",
    "{user1} subjected {user2} to a fiery furnace.",
    "Sakura Haruno just got more useful than {user2}",
    "{user1} unplugged {user2}'s life support.",
    "{user1} subscribed {user2}' to 5 years of bad internet.",
    "{user1} learned why being a crocodile dentist was a bad idea.",
    "You know what’s worse than Dad jokes? {user2}!",
    "{user1} took all of {user2}'s cookies.",
)


ITEMS = (
    "cast iron skillet",
    "angry meow",
    "cricket bat",
    "wooden cane",
    "shovel",
    "toaster",
    "book",
    "laptop",
    "rubber chicken",
    "spiked bat",
    "heavy rock",
    "chunk of dirt",
    "ton of bricks",
    "rasengan",
    "spirit bomb",
    "100-Type Guanyin Bodhisattva",
    "rasenshuriken",
    "Murasame",
    "ban",
    "chunchunmaru",
    "Kubikiribōchō",
    "rasengan",
    "spherical flying kat",
)


THROW = (
    "throws",
    "flings",
    "chucks",
    "hurls",
)


HIT = ("hits", "whacks", "slaps", "smacks", "bashes", "pats")


REACTIONS = (
    "( ͡° ͜ʖ ͡°)",
    "( . •́ _ʖ •̀ .)",
    "( ಠ ͜ʖ ಠ)",
    "( ͡ ͜ʖ ͡ )",
    "(ʘ ͜ʖ ʘ)",
    "ヾ(´〇`)ﾉ♪♪♪",
    "ヽ(o´∀`)ﾉ♪♬",
    "♪♬((d⌒ω⌒b))♬♪",
    "└(＾＾)┐",
    "(￣▽￣)/♫•*¨*•.¸¸♪",
    "ヾ(⌐■_■)ノ♪",
    "乁( • ω •乁)",
    "♬♫♪◖(● o ●)◗♪♫♬",
    "(っ˘ڡ˘ς)",
    "( ˘▽˘)っ♨",
    "(　・ω・)⊃-[二二]",
    "(*´ー`)旦 旦(￣ω￣*)",
    "( ￣▽￣)[] [](≧▽≦ )",
    "(*￣▽￣)旦 且(´∀`*)",
    "(ノ ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ",
    "(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆",
    "(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
    "(∩` ﾛ ´)⊃━炎炎炎炎炎",
    "( ・∀・)・・・--------☆",
    "( -ω-)／占~~~~~",
    "○∞∞∞∞ヽ(^ー^ )",
    "(*＾＾)/~~~~~~~~~~◎",
    "((( ￣□)_／",
    "(ﾒ￣▽￣)︻┳═一",
    "ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ",
    "(*`0´)θ☆(メ°皿°)ﾉ",
    "(; -_-)――――――C<―_-)",
    "ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )",
    "(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/",
    "/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)",
    "(`⌒*)O-(`⌒´Q)",
    "(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง",
    "ヾ(・ω・)メ(・ω・)ノ",
    "(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ",
    "ヽ( ⌒ω⌒)人(=^‥^= )ﾉ",
    "｡*:☆(・ω・人・ω・)｡:゜☆｡",
    "(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)",
    "(っ˘▽˘)(˘▽˘)˘▽˘ς)",
    "(*＾ω＾)人(＾ω＾*)",
    r"＼(▽￣ \ (￣▽￣) / ￣▽)／",
    "(￣Θ￣)",
    "＼( ˋ Θ ´ )／",
    "( ´(00)ˋ )",
    "＼(￣(oo)￣)／",
    "／(≧ x ≦)＼",
    "／(=･ x ･=)＼",
    "(=^･ω･^=)",
    "(= ; ｪ ; =)",
    "(=⌒‿‿⌒=)",
    "(＾• ω •＾)",
    "ଲ(ⓛ ω ⓛ)ଲ",
    "ଲ(ⓛ ω ⓛ)ଲ",
    "(^◔ᴥ◔^)",
    "[(－－)]..zzZ",
    "(￣o￣) zzZZzzZZ",
    "(＿ ＿*) Z z z",
    "☆ﾐ(o*･ω･)ﾉ",
    "ε=ε=ε=ε=┌(;￣▽￣)┘",
    "ε===(っ≧ω≦)っ",
    "__φ(．．)",
    "ヾ( `ー´)シφ__",
    "( ^▽^)ψ__",
    "|･ω･)",
    "|д･)",
    "┬┴┬┴┤･ω･)ﾉ",
    "|･д･)ﾉ",
    "(*￣ii￣)",
    "(＾〃＾)",
    "m(_ _)m",
    "人(_ _*)",
    "(シ. .)シ",
    "(^_~)",
    "(>ω^)",
    "(^_<)〜☆",
    "(^_<)",
    "(づ￣ ³￣)づ",
    "(⊃｡•́‿•̀｡)⊃",
    "⊂(´• ω •`⊂)",
    "(*・ω・)ﾉ",
    "(^-^*)/",
    "ヾ(*'▽'*)",
    "(^０^)ノ",
    "(*°ｰ°)ﾉ",
    "(￣ω￣)/",
    "(≧▽≦)/",
    "w(°ｏ°)w",
    "(⊙_⊙)",
    "(°ロ°) !",
    "∑(O_O;)",
    "(￢_￢)",
    "(¬_¬ )",
    "(↼_↼)",
    "(￣ω￣;)",
    "┐('～`;)┌",
    "(・_・;)",
    "(＠_＠)",
    "(•ิ_•ิ)?",
    "ヽ(ー_ー )ノ",
    "┐(￣ヘ￣)┌",
    "┐(￣～￣)┌",
    "┐( ´ д ` )┌",
    "╮(︶▽︶)╭",
    "ᕕ( ᐛ )ᕗ",
    "(ノωヽ)",
    "(″ロ゛)",
    "(/ω＼)",
    "(((＞＜)))",
    "~(>_<~)",
    "(×_×)",
    "(×﹏×)",
    "(ノ_<。)",
    "(μ_μ)",
    "o(TヘTo)",
    "( ﾟ，_ゝ｀)",
    "( ╥ω╥ )",
    "(／ˍ・、)",
    "(つω`｡)",
    "(T_T)",
    "o(〒﹏〒)o",
    "(＃`Д´)",
    "(・`ω´・)",
    "( `ε´ )",
    "(ﾒ` ﾛ ´)",
    "Σ(▼□▼メ)",
    "(҂ `з´ )",
    "٩(╬ʘ益ʘ╬)۶",
    "↑_(ΦwΦ)Ψ",
    "(ﾉಥ益ಥ)ﾉ",
    "(＃＞＜)",
    "(；￣Д￣)",
    "(￢_￢;)",
    "(＾＾＃)",
    "(￣︿￣)",
    "ヾ( ￣O￣)ツ",
    "(ᗒᗣᗕ)՞",
    "(ノ_<。)ヾ(´ ▽ ` )",
    "ヽ(￣ω￣(。。 )ゝ",
    "(ﾉ_；)ヾ(´ ∀ ` )",
    "(´-ω-`( _ _ )",
    "(⌒_⌒;)",
    "(*/_＼)",
    "( ◡‿◡ *)",
    "(//ω//)",
    "(￣▽￣*)ゞ",
    "(„ಡωಡ„)",
    "(ﾉ´ з `)ノ",
    "(♡-_-♡)",
    "(─‿‿─)♡",
    "(´ ω `♡)",
    "(ღ˘⌣˘ღ)",
    "(´• ω •`) ♡",
    "╰(*´︶`*)╯♡",
    "(≧◡≦) ♡",
    "♡ (˘▽˘>ԅ( ˘⌣˘)",
    "σ(≧ε≦σ) ♡",
    "(˘∀˘)/(μ‿μ) ❤",
    "Σ>―(〃°ω°〃)♡→",
    "(* ^ ω ^)",
    "(o^▽^o)",
    "ヽ(・∀・)ﾉ",
    "(o･ω･o)",
    "(^人^)",
    "( ´ ω ` )",
    "(´• ω •`)",
    "╰(▔∀▔)╯",
    "(✯◡✯)",
    "(⌒‿⌒)",
    "(*°▽°*)",
    "(´｡• ᵕ •｡`)",
    "ヽ(>∀<☆)ノ",
    "＼(￣▽￣)／",
    "(o˘◡˘o)",
    "(╯✧▽✧)╯",
    "( ‾́ ◡ ‾́ )",
    "(๑˘︶˘๑)",
    "(´･ᴗ･ ` )",
    "( ͡° ʖ̯ ͡°)",
    "( ఠ ͟ʖ ఠ)",
    "( ಥ ʖ̯ ಥ)",
    "(≖ ͜ʖ≖)",
    "ヘ(￣ω￣ヘ)",
    "(ﾉ≧∀≦)ﾉ",
    "└(￣-￣└))",
    "┌(＾＾)┘",
    "(^_^♪)",
    "(〜￣△￣)〜",
    "(｢• ω •)｢",
    "( ˘ ɜ˘) ♬♪♫",
    "( o˘◡˘o) ┌iii┐",
    "♨o(>_<)o♨",
    "( ・・)つ―{}@{}@{}-",
    "(*´з`)口ﾟ｡ﾟ口(・∀・ )",
    "( *^^)o∀*∀o(^^* )",
    "-●●●-ｃ(・・ )",
    "(ﾉ≧∀≦)ﾉ ‥…━━━★",
    "╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ",
    "(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)",
)


TOSS = (
    "Heads",
    "Tails",
)


DECIDE = ("Yes.", "No.", "Maybe.")
