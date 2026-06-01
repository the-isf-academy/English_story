from model_story import Story

main_story = Story(
    title="Invisible Weight",

    first_id="cricket",
    first_title="Cricket Club",

    first_description="""
And when the cricket club coach says,
“You girls are only here to date the boys,”

you look around and hope that by sitting in silence
no one will ask why you are not laughing.

You wonder whether the boys hear the same thing
or whether this moment is reserved only for you.
"""
)

# -------------------------
# CHAPTER 1: CRICKET CLUB
# -------------------------

main_story.add_choice(
    "cricket",
    "Stay silent and look down",
    "socks",

    fatigue_change=2,
    belonging_change=-2,
    selfworth_change=-1
)

main_story.add_choice(
    "cricket",
    "Force a small laugh to blend in",
    "socks",

    fatigue_change=1,
    belonging_change=1,
    tension_change=2
)

main_story.add_choice(
    "cricket",
    "Speak up: 'That’s not why I’m here.'",
    "socks",

    fatigue_change=1,
    tension_change=3,
    selfworth_change=2,
    belonging_change=-1
)

# -------------------------
# CHAPTER 2: SOCKS
# -------------------------

main_story.add_node(
    "socks",
    "School Office",
    """
You take yourself to school and sit through history,
then math, then English.

A man you’ve never seen before calls you out of class.

“You need to change your socks,” he says.

“Why?”

“Your ankles might be distracting.”

You can’t help but giggle, a nervous sound that escapes
before you can stop it.

He doesn’t even smile.

And you realise that something, someone,
made him think this is okay.
"""
)

main_story.add_choice(
    "socks",
    "Stay silent and go change your socks",
    "bill",

    fatigue_change=2,
    selfworth_change=-2,
    belonging_change=-1
)

main_story.add_choice(
    "socks",
    "Ask: 'Are you actually serious?'",
    "bill",

    tension_change=3,
    selfworth_change=1,
    fatigue_change=1
)

main_story.add_choice(
    "socks",
    "Refuse and storm back to class",
    "bill",

    fatigue_change=2,
    tension_change=2,
    belonging_change=-1
)

# -------------------------
# CHAPTER 3: RESTAURANT BILL
# -------------------------

main_story.add_node(
    "bill",
    "Dinner Table",
    """
You wave to the waiter and a man comes over.

You tell him you want to pay.

He returns and presents the bill to your father sitting across from you.

And although your father passes the bill to you,
you begin to think, maybe erroneously, that there was nothing wrong.

Then a voice in your head tells you to take your foot off your throat,
because it’s just a dinner and you don’t want to bring any more trouble.
"""
)

main_story.add_choice(
    "bill",
    "Say nothing and pay quietly",
    "loss",

    fatigue_change=2,
    selfworth_change=-1,
    tension_change=1
)

main_story.add_choice(
    "bill",
    "Point out: 'I asked for the bill. Why did you give it to my dad?'",
    "loss",

    tension_change=2,
    selfworth_change=2,
    belonging_change=-1
)

main_story.add_choice(
    "bill",
    "Laugh it off and leave no tip",
    "loss",

    fatigue_change=1,
    belonging_change=1,
    selfworth_change=-1
)

# -------------------------
# CHAPTER 4: NEIGHBOUR
# -------------------------

main_story.add_node(
    "loss",
    "After the Funeral",
    """
When your stepfather suddenly passes away,
your neighbor comes over with ribs and asks your mom
if your family will move somewhere a little less fancy.

You push past your mom and tell him your family is perfectly capable.

He stutters: “I was just trying to take care of you all.”

The rain seems to blow into the house,
and wets your shirt until you realise it wasn’t rain after all.

The body keeps score of what the mind forgets.
"""
)

main_story.add_choice(
    "loss",
    "Push back: 'We don’t need your misogynistic thoughts.'",
    "colleague",

    tension_change=3,
    selfworth_change=2,
    fatigue_change=2
)

main_story.add_choice(
    "loss",
    "Stay quiet behind your mom",
    "colleague",

    fatigue_change=2,
    selfworth_change=-2,
    belonging_change=-1
)

main_story.add_choice(
    "loss",
    "Apologize and accept the food",
    "colleague",

    fatigue_change=3,
    tension_change=1,
    selfworth_change=-3
)

# -------------------------
# CHAPTER 5: COLLEAGUE
# -------------------------

main_story.add_node(
    "colleague",
    "Work Conversation",
    """
Your younger male colleague says women lose all value after 25.

A divorced woman is like a used car, he says.

The words sit in the air like something rotten.
"""
)

main_story.add_choice(
    "colleague",
    "Stay silent",
    "drive",

    fatigue_change=2,
    selfworth_change=-2,
    tension_change=2
)

main_story.add_choice(
    "colleague",
    "Call it out",
    "drive",

    tension_change=3,
    selfworth_change=2,
    fatigue_change=1
)

main_story.add_choice(
    "colleague",
    "Laugh it off",
    "drive",

    fatigue_change=2,
    belonging_change=1,
    selfworth_change=-1
)

# -------------------------
# CHAPTER 6: DRIVE THROUGH
# -------------------------

main_story.add_node(
    "drive",
    "Drive Through",
    """
In line at the drive through, it is finally your turn.

An old man looks at you and says:

“Isn’t this car too big for you?”

You stare at him.

The transaction goes swiftly after that.
"""
)

main_story.add_choice(
    "drive",
    "Drive away without ordering",
    "professor",

    fatigue_change=2,
    selfworth_change=-1,
    tension_change=2
)

main_story.add_choice(
    "drive",
    "Respond: 'Excuse me?'",
    "professor",

    tension_change=3,
    selfworth_change=1,
    fatigue_change=2
)

main_story.add_choice(
    "drive",
    "Joke: 'Of course I can'",
    "professor",

    fatigue_change=1,
    belonging_change=1,
    selfworth_change=-3
)

# -------------------------
# CHAPTER 7: PROFESSOR
# -------------------------

main_story.add_node(
    "professor",
    "Meeting Room",
    """
You eat quietly at the corner of a meeting room.

A professor shows you a picture of his wife.

“She is a beautiful and intelligent woman,” he says,
“and of course, merely a researcher. Unlike me.”
"""
)

main_story.add_choice(
    "professor",
    "Stay silent and nod",
    "counselor",

    fatigue_change=2,
    selfworth_change=-1,
    tension_change=1
)

main_story.add_choice(
    "professor",
    "Question him",
    "counselor",

    tension_change=2,
    selfworth_change=2,
    fatigue_change=1
)

main_story.add_choice(
    "professor",
    "Change the subject",
    "counselor",

    fatigue_change=1,
    belonging_change=1,
    selfworth_change=-1
)

# -------------------------
# CHAPTER 8: COUNSELOR
# -------------------------

main_story.add_node(
    "counselor",
    "University Counselor",
    """
The counselor tells you medicine is unrealistic.

You say your name.

He reacts like it doesn’t fit what he expected.

“You are Charlie Pienaar?” he says.

Then everything pauses.
"""
)

main_story.add_choice(
    "counselor",
    "Leave quietly",
    "tv",

    fatigue_change=3,
    selfworth_change=-2,
    tension_change=2
)

main_story.add_choice(
    "counselor",
    "Correct him firmly",
    "tv",

    tension_change=3,
    selfworth_change=2,
    fatigue_change=1
)

main_story.add_choice(
    "counselor",
    "Say you'll consider nursing",
    "tv",

    fatigue_change=2,
    selfworth_change=-3,
    belonging_change=1
)

# -------------------------
# CHAPTER 9: TELEVISION
# -------------------------

main_story.add_node(
    "tv",
    "Late Night Television",
    """
And when the rocket scientists asked Sally Ride whether 100 tampons
would be enough for a week-long space mission, you fumble for the remote.

You mute the TV for a second, then hesitate.

It is all too exhausting.

You realise perhaps each sigh is drawn into existence
to pull in, pull under, who knows.

Truth be told, you could no more control those sighs
than that which brings them about.
"""
)

main_story.add_choice(
    "tv",
    "Turn off the TV and disengage",
    None,

    fatigue_change=2,
    selfworth_change=-2,
    belonging_change=-2
)

main_story.add_choice(
    "tv",
    "Turn the volume back on and keep watching",
    None,

    fatigue_change=3,
    belonging_change=1,
    tension_change=1
)

main_story.add_choice(
    "tv",
    "Post on Instagram about their lack of knowledge",
    None,

    tension_change=3,
    selfworth_change=2,
    fatigue_change=4
)