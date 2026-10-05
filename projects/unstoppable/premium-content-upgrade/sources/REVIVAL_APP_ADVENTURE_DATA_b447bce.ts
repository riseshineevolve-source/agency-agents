// Character definitions - Project Unstoppable uses Dilo and Luli
export const characters = {
  dilo: {
    name: "Dilo",
    color: "orange",
    hsl: "25 95% 55%",
    role: "PIXEL SPIKER",
    description: "Your tech-savvy guide through the digital landscape of growing up.",
    traits: ["Goal Goblin", "Level Crusher", "Style General", "Stubborn Star", "Treat Dealer"],
  },
  luli: {
    name: "Luli",
    color: "amber",
    hsl: "45 95% 55%",
    role: "CREATIVE GLOW",
    description: "Your creative and stylish companion for navigating life's challenges.",
    traits: ["Mystery Brain", "Style Queen", "Clue Collector", "Idea Whisperer", "Book Diver"],
  },
};

export type CharacterKey = keyof typeof characters;

// Book cover / Intro
export const bookCover = {
  warning: "WARNING: This is NOT a boring school book.",
  tagline: "We have a massive secret to share. Most people think adventures only happen in movies. BUT WE KNOW THE TRUTH: Every single day can be legendary if you unlock the superpowers you already have inside.",
  mainMessage: [
    "Consider this book your personal 'SURVIVAL KIT'.",
    "We – The Happy-Makers – are here to help you build your strength, find your calm, and turn the ordinary into the SPECTACULAR.",
    "YOU ARE THE CAPTAIN.",
    "Are you ready to unlock your inner Legend?",
  ],
  callToAction: "LET'S LAUNCH INTO THE FUTURE – TOGETHER!",
  motto: "PROJECT UNSTOPPABLE",
};

export const dedication = {
  title: "DEDICATION",
  belongsTo: "This project belongs to YOU.",
  dedicatedTo: [
    "The Gamer inside you looking for cheat codes.",
    "The Chaos Manager trying to balance school and life.",
    "The Future Boss who has big dreams.",
  ],
  grownUps: "Authorized Personnel Only. This contains top-secret strategies.",
  signoff: "YOU ARE THE CAPTAIN.",
};

export const introduction = {
  title: "WELCOME, LEGENDS!",
  content: [
    "WARNING: This is NOT a boring school book.",
    "We have a massive secret to share. Most people think adventures only happen in movies. BUT WE KNOW THE TRUTH: Every single day can be legendary if you unlock the superpowers you already have inside.",
    "Consider this book your personal 'SURVIVAL KIT'.",
    "We – The Happy-Makers – are here to help you build your strength, find your calm, and turn the ordinary into the SPECTACULAR.",
  ],
  signoff: "YOU ARE THE CAPTAIN. Are you ready to unlock your inner Legend? LET'S LAUNCH INTO THE FUTURE – TOGETHER!",
};

export const howToUseIt = {
  title: "HOW TO USE THIS APP",
  subtitle: "Your Daily Mission Structure",
  intro: "Each day has 6 sections designed to level up your life skills. Take about 10 minutes per day.",
  description: "This isn't homework. Think of it as your personal training program for becoming unstoppable.",
  dailyMission: {
    title: "Each Daily Mission includes:",
    parts: [
      { name: "INTRO", description: "A character connects with you and drops some real talk." },
      { name: "BRIEFING", description: "Your main quest plus an XP Boost challenge." },
      { name: "WORKBENCH", description: "A Tool for Life you can use forever (your rescue kit)." },
      { name: "SYSTEM REBOOT", description: "A short reset exercise to slow down and refocus." },
      { name: "GLITCH & PUZZLE", description: "A cheat code quote plus a brain puzzle." },
      { name: "FREE ROAM", description: "Your space for notes, doodles, and brain dumps." },
    ],
  },
  tips: [
    { title: "BE HONEST", content: "No one's reading this but you. Write what you actually think." },
    { title: "10 MINUTES MAX", content: "Quick sessions can be easier to stick with than long boring ones." },
    { title: "USE IT DAILY", content: "Consistency beats intensity. Show up every day." },
    { title: "HAVE FUN", content: "If it feels like homework, you're doing it wrong. Add your style." },
  ],
};

// Week/phase definitions
export const weeks = [
  {
    number: 1,
    title: "Identity & Self-Discovery",
    subtitle: "Define Your Avatar",
    description: "Figure out who you really are, what makes you tick, and stop pretending to be someone else.",
    motto: "CUSTOMIZE YOUR CHARACTER. STOP BEING A COPY OF A COPY.",
    days: [1, 2, 3, 4],
  },
  {
    number: 2,
    title: "Resilience & Communication",
    subtitle: "Level Up Your Shield",
    description: "Deal with haters, understand parents, rest properly, and hack your brain for better learning.",
    motto: "BUILD YOUR SHIELD. HACK YOUR BRAIN. BECOME UNSTOPPABLE.",
    days: [5, 6, 7],
  },
  {
    number: 3,
    title: "Brain & Time Mastery",
    subtitle: "Hack Your System",
    description: "Master study hacks, time management, beat procrastination, and break big projects into bits.",
    motto: "WORK LIKE A SNIPER, NOT A MACHINE GUN.",
    days: [8, 9, 10, 11],
  },
  {
    number: 4,
    title: "Life Systems & Focus",
    subtitle: "Optimize Your Server",
    description: "Bio-hack your mornings, build a focus fortress, and celebrate your progress.",
    motto: "PROTECT YOUR MORNINGS. WIN THE DAY.",
    days: [12, 13, 14],
  },
  {
    number: 5,
    title: "Power & Money",
    subtitle: "Boss Mode Activated",
    description: "Learn to say no, manage money, budget like a CEO, and take responsibility.",
    motto: "YOUR ENERGY IS EXPENSIVE. SPEND IT WISELY.",
    days: [15, 16, 17, 18],
  },
  {
    number: 6,
    title: "Effectiveness & Purpose",
    subtitle: "Find Your Mission",
    description: "Focus on what matters, discover talents, build a vision board, and set real goals.",
    motto: "DO LESS, BUT BETTER. FIND YOUR IKIGAI.",
    days: [19, 20, 21, 22, 23, 24],
  },
  {
    number: 7,
    title: "Legacy & Launch",
    subtitle: "Become Unstoppable",
    description: "Embrace failure, find mentors, make impact, build your legacy, practice gratitude, and launch.",
    motto: "YOU ARE UNSTOPPABLE.",
    days: [25, 26, 27, 28, 29, 30, 31],
  },
];

// Interactive elements for missions
export interface InteractiveElement {
  type: "choice" | "text" | "checklist" | "slider" | "drawing" | "scramble" | "matching" | "timed" | "simon" | "dots" | "trivia" | "memory";
  id: string;
  prompt: string;
  options?: string[];
  placeholder?: string;
  min?: number;
  max?: number;
  // New game types
  word?: string;
  scrambleHint?: string;
  pairs?: { left: string; right: string }[];
  timeLimit?: number;
  tasks?: { prompt: string; type: "tap" | "text"; answer?: string }[];
  targetSequenceLength?: number;
  dots?: { x: number; y: number }[];
  questions?: { question: string; options: string[]; correctAnswerIndex: number }[];
  cards?: string[];
}

// Day content structure
export interface DayContent {
  day: number;
  title: string;
  character: CharacterKey;
  weekNumber: number;
  sections: {
    intro: {
      characterConnecting: string;
      message: string;
      quote: string;
      quoteAuthor: string;
    };
    briefing: {
      questTitle: string;
      steps: string[];
      xpBoost: string;
      interactive: InteractiveElement[];
    };
    workbench: {
      toolTitle: string;
      whenToUse: string;
      howToUse: string;
      yourTurn: string;
      interactive: InteractiveElement[];
    };
    systemReboot: {
      title: string;
      instructions: string;
    };
    glitchPuzzle: {
      cheatCode: string;
      puzzleTitle: string;
      puzzleContent: string;
      interactive: InteractiveElement[];
    };
    freeRoam: {
      title: string;
    };
  };
}

export const dayContents: Record<number, DayContent> = {
  1: {
    day: 1, title: "The Avatar Setup", character: "dilo", weekNumber: 1,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Stop trying to be a copy of a copy. In life, customizing your character is mandatory. If you don't define who you are, the algorithm (and your family) will guess. And they usually guess wrong. It's time to publish your specs.",
        quote: "YOU DO NOT NEED TO BECOME SOMEONE ELSE TO START BUILDING A STRONGER VERSION OF YOU.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Family Press Release",
        steps: [
          "THE CORE: Write down your top 3 Values (e.g., 'Honesty, Humor, Freedom').",
          "THE BRIEF: Go to your parents. Tell them: 'I am updating my Avatar. These 3 things are important to me now.'",
          "THE ASK: Ask them: 'What is ONE value you think fits me perfectly?' Write it down.",
        ],
        xpBoost: "Grab your phone right now. Find 3 social media accounts that make you feel bad about yourself. UNFOLLOW or MUTE them. Don't think twice. Bye, Felicia.",
        interactive: [
          { type: "text", id: "d1_values", prompt: "Write your top 3 values:", placeholder: "e.g., Honesty, Humor, Freedom" },
          { type: "text", id: "d1_parent_value", prompt: "What value did your parent say fits you?", placeholder: "Type their answer..." },
          { type: "checklist", id: "d1_unfollow", prompt: "Social media cleanup:", options: ["Unfollowed account #1", "Unfollowed account #2", "Unfollowed account #3"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "Whenever you feel pressured to fit in or fake who you are.",
        howToUse: "Open this page. Read your Values. Say: 'Does this decision match my Avatar?' If no, delete it.",
        yourTurn: "Draw your specs. Map out the values.",
        interactive: [
          { type: "drawing", id: "d1_avatar", prompt: "Draw your Avatar specs below:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Safe Server",
        instructions: "Close your eyes. Imagine a place (real or made up) where no one can track you. No notifications. No drama. Just you. What does it smell like? What sounds do you hear? This is your private server. Visit it whenever the main lobby gets too loud.",
      },
      glitchPuzzle: {
        cheatCode: "IF A CHOICE DOESN'T MATCH YOUR SPECS, IT'S A GLITCH. DELETE IT.",
        puzzleTitle: "PUZZLE: The Mirror Code",
        puzzleContent: "Below is a message written backwards. Decode it:",
        interactive: [
          { type: "text", id: "d1_puzzle", prompt: ".thgir si tahw od ot egaruoc eht evah I", placeholder: "Type the decoded message..." },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  2: {
    day: 2, title: "Strengths & Glitches", character: "luli", weekNumber: 1,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Here is the tea: There are no 'flaws', only features in the wrong context. You think you're 'bossy'? No, you have Leadership Skills. You're 'too quiet'? You have Observation Skills. Let's rebrand your glitches.",
        quote: "A TRAIT CAN FEEL LIKE A BUG IN ONE SITUATION AND BECOME A STRENGTH IN ANOTHER.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Feature/Bug List",
        steps: [
          "THE BUGS: List 3 things you consider weaknesses.",
          "THE PATCH: Rewrite them as 'Features' (Strengths). Example: Stubborn → Persistent.",
        ],
        xpBoost: "Text a family member: 'Hey, quick question: What do you think is my superpower?' Write down their answer.",
        interactive: [
          { type: "text", id: "d2_bug1", prompt: "Bug #1 → Feature:", placeholder: "e.g., Stubborn → Persistent" },
          { type: "text", id: "d2_bug2", prompt: "Bug #2 → Feature:", placeholder: "e.g., Too quiet → Observant" },
          { type: "text", id: "d2_bug3", prompt: "Bug #3 → Feature:", placeholder: "e.g., Bossy → Leader" },
          { type: "text", id: "d2_superpower", prompt: "What superpower did they say?", placeholder: "Their answer..." },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel 'not good enough' or make a mistake.",
        howToUse: "Re-read your 'Features'. Remind yourself that every hero has a weakness. It's part of the plot.",
        yourTurn: "Transform your glitches into superpowers. Draw two columns: BUGS vs FEATURES.",
        interactive: [
          { type: "drawing", id: "d2_bugs_features", prompt: "Draw your BUGS vs FEATURES columns:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Archive",
        instructions: "Think of a cringe memory. Imagine putting it into a folder named 'OLD FILES'. Right-click. Select 'ARCHIVE'. It is just data now. It doesn't slow down your RAM anymore.",
      },
      glitchPuzzle: {
        cheatCode: "DON'T FIX YOUR BUGS. MAX OUT YOUR FEATURES. THAT'S HOW YOU WIN.",
        puzzleTitle: "PUZZLE: The Binary Labyrinth",
        puzzleContent: "Imagine a maze where you can only turn right at '1' and left at '0'. Sequence: 1-0-1-1-0-1",
        interactive: [
          { type: "choice", id: "d2_puzzle", prompt: "Which direction do you end up facing?", options: ["North", "East", "South", "West"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  3: {
    day: 3, title: "The Emotion Dashboard", character: "dilo", weekNumber: 1,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Your body gives you clues about how you're doing. Sweaty hands can show up with stress or excitement. Tired eyes can mean you need a break. Noticing signals early can help you choose what to do next.",
        quote: "FEELINGS ARE SIGNALS TO NOTICE, NOT LABELS THAT DEFINE YOU.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: Map the Sensors",
        steps: [
          "On the body map, use patterns to show where you feel: ANGER (Fists?), ANXIETY (Stomach knots?)",
          "Create one 'Emergency Protocol' for the strongest one.",
        ],
        xpBoost: "The next time you feel a strong emotion today, pause and say out loud: 'I am detecting [Emotion Name].' Don't fix it, just name it.",
        interactive: [
          { type: "choice", id: "d3_anger", prompt: "Where do you feel ANGER?", options: ["Head", "Chest", "Fists", "Stomach", "Everywhere"] },
          { type: "choice", id: "d3_anxiety", prompt: "Where do you feel ANXIETY?", options: ["Stomach", "Chest", "Throat", "Hands", "Legs"] },
          { type: "text", id: "d3_protocol", prompt: "Your Emergency Protocol:", placeholder: "When I feel [emotion], I will..." },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel overwhelmed by feelings you can't name.",
        howToUse: "Scan your body. Where is the feeling? Name it to tame it.",
        yourTurn: "Color your dashboard. Where do your feelings live?",
        interactive: [
          { type: "drawing", id: "d3_body_map", prompt: "Draw your emotion body map:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Power Pose",
        instructions: "Stand up in a steady posture for 2 minutes: feet planted, shoulders relaxed, chin level. Notice whether your breathing or sense of readiness changes. No magic — just a quick body check-in.",
      },
      glitchPuzzle: {
        cheatCode: "EMOTIONS ARE JUST DATA. READ THEM, BUT DON'T LET THEM DRIVE.",
        puzzleTitle: "PUZZLE: Emoji Decoder",
        puzzleContent: "Guess the emotion based on the equation:",
        interactive: [
          { type: "text", id: "d3_emoji1", prompt: "🔥 + ✊ = ?", placeholder: "What emotion?" },
          { type: "text", id: "d3_emoji2", prompt: "🌧️ + 🛏️ = ?", placeholder: "What emotion?" },
          { type: "text", id: "d3_emoji3", prompt: "🦋 + 🎤 = ?", placeholder: "What emotion?" },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  4: {
    day: 4, title: "Squad Analysis", character: "luli", weekNumber: 1,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Your squad determines your stats. But guess what? Your family is your 'Default Squad'. You didn't choose them in the lobby, but you are on the same server. Let's optimize this team.",
        quote: "PAY ATTENTION TO WHO HELPS YOU FEEL SAFE, RESPECTED, AND MORE LIKE YOURSELF.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Family Vibe Check",
        steps: [
          "AUDIT: Look at your family. Who is the 'Funny One'? The 'Stressed One'?",
          "THE UPGRADE: Identify one person you want to be closer to.",
          "ACTION: Ask them for a '3-Minute Podcast'. Ask ONE question: 'What was your favorite song when you were my age?' Listen.",
        ],
        xpBoost: "Send a meme or a funny video to your family group chat. Laughter creates an instant connection bridge.",
        interactive: [
          { type: "text", id: "d4_funny", prompt: "Who is the 'Funny One'?", placeholder: "Name..." },
          { type: "text", id: "d4_closer", prompt: "Who do you want to be closer to?", placeholder: "Name..." },
          { type: "text", id: "d4_song", prompt: "What was their favorite song?", placeholder: "Their answer..." },
          { type: "checklist", id: "d4_meme", prompt: "XP Boost:", options: ["Sent a meme to the family group chat"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel lonely.",
        howToUse: "Look at your 'Center Circle'. Pick one person. Text them.",
        yourTurn: "Map your Squad. Draw the 3 circles. Put family members in too.",
        interactive: [
          { type: "drawing", id: "d4_squad_map", prompt: "Draw your Squad Map with 3 circles:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Connection Cord",
        instructions: "Close your eyes. Visualize a glowing cord connecting you to your best friend. Send a pulse of bright light through that cord. Feel the warmth come back.",
      },
      glitchPuzzle: {
        cheatCode: "IF YOU HAVE TO FAKE WHO YOU ARE TO STAY IN THE SQUAD, LOG OUT.",
        puzzleTitle: "PUZZLE: Friendship Logic",
        puzzleContent: "Alex hates computers. Ben is always moving.",
        interactive: [
          { type: "choice", id: "d4_alex", prompt: "Best hobby for Alex?", options: ["Coding", "Sports", "Painting", "Gaming"] },
          { type: "choice", id: "d4_ben", prompt: "Best hobby for Ben?", options: ["Reading", "Dance", "Chess", "Cooking"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  5: {
    day: 5, title: "The Hater Blocker", character: "dilo", weekNumber: 2,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Mean comments can feel like lag: distracting, annoying, and sometimes painful. You cannot know exactly why someone said them, so separate what happened from the story you tell yourself about it.",
        quote: "SOMEONE ELSE'S PUT-DOWN DOES NOT GET TO DECIDE YOUR VALUE.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Teflon Shield",
        steps: [
          "Write down a mean comment you've received or heard.",
          "SEPARATE FACT FROM GUESS: What was actually said? What do you know about yourself that the comment does not get to decide?",
          "Design your 'Mental Shield' symbol.",
        ],
        xpBoost: "For low-stakes baiting, practice a calm, boring response for 30 seconds. If it is repeated bullying, threatening, sexual, discriminatory, or makes you feel unsafe, block/report it and tell a trusted adult or school staff member.",
        interactive: [
          { type: "text", id: "d5_mean", prompt: "A mean comment:", placeholder: "What they said..." },
          { type: "text", id: "d5_translate", prompt: "Fact vs. guess:", placeholder: "What happened? What does NOT get to define you?" },
          { type: "drawing", id: "d5_shield", prompt: "Design your Mental Shield:" },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When someone insults you.",
        howToUse: "For low-stakes insults, pause before reacting and return to what you know is true. For bullying or threats, save evidence, block/report where possible, and get a trusted adult involved.",
        yourTurn: "Draw your Shield. Write the Truths inside.",
        interactive: [
          { type: "drawing", id: "d5_shield_draw", prompt: "Draw your Shield with Truths inside:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Force Field",
        instructions: "Sit quietly. Imagine a glowing bubble around you and let mean words bounce away like confetti. This is a calming exercise, not a safety plan — if a situation is unsafe, get help.",
      },
      glitchPuzzle: {
        cheatCode: "DON'T FEED THE TROLLS. BLOCK, REPORT, AND GET HELP WHEN YOU NEED IT.",
        puzzleTitle: "PUZZLE: Spot the Difference",
        puzzleContent: "Two shield images — find 7 differences between the shields below.",
        interactive: [
          { type: "slider", id: "d5_differences", prompt: "How many differences did you find?", min: 0, max: 7 },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  6: {
    day: 6, title: "Parent Translator", character: "luli", weekNumber: 2,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Sometimes adults repeat themselves and it lands as nagging. There may be a concern or goal underneath — but do not mind-read. Ask what matters to them, then explain what matters to you.",
        quote: "GOOD COMMUNICATION STARTS WITH SAYING WHAT YOU MEAN AND LISTENING FOR WHAT THE OTHER PERSON MEANS.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The 'Adult' Interview",
        steps: [
          "Flip the script. Become the Journalist. Find a parent.",
          "Ask: 'What was the biggest trouble you got into when you were my age?'",
          "Ask: 'What were you most scared of?'",
        ],
        xpBoost: "Use the 'I Hear You' Hack. Try: 'I hear that [X] matters to you. Can I tell you my plan?'",
        interactive: [
          { type: "text", id: "d6_trouble", prompt: "Their biggest trouble:", placeholder: "What they told you..." },
          { type: "text", id: "d6_scared", prompt: "What were they most scared of?", placeholder: "Their answer..." },
          { type: "checklist", id: "d6_hack", prompt: "Did you try the hack?", options: ["Used 'I Hear You' on a parent"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When a conversation with a parent or caregiver is getting tense.",
        howToUse: "Pause. Ask what the concern is, then explain your side without guessing what they think.",
        yourTurn: "Write down the 'Nag' vs. The 'Real Meaning'.",
        interactive: [
          { type: "text", id: "d6_nag1", prompt: "Nag: 'Clean your room!' → Real meaning:", placeholder: "They want..." },
          { type: "text", id: "d6_nag2", prompt: "Nag: 'Get off your phone!' → Real meaning:", placeholder: "They worry about..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Empathy Switch",
        instructions: "Think of a recent disagreement. What information might you have that the other person missed? What information might they have that you missed? Pick one calm question you could ask.",
      },
      glitchPuzzle: {
        cheatCode: "THE CURRENCY OF FREEDOM IS TRUST. PAY WITH TASKS, BUY FREEDOM.",
        puzzleTitle: "PUZZLE: Code Breaker",
        puzzleContent: "Translate parent-speak into real talk:",
        interactive: [
          { type: "choice", id: "d6_puzzle1", prompt: "If you hear 'Because I said so' and it is safe to discuss later, the most useful next move is:", options: ["Guess what they secretly mean", "Ask when you can talk about the reason", "Shout louder", "Pretend you agreed"] },
          { type: "choice", id: "d6_puzzle2", prompt: "When an adult compares today with 'when I was your age,' a useful move is:", options: ["Assume they are judging you", "Listen, then explain what is different now", "End the conversation immediately", "Agree with everything"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  7: {
    day: 7, title: "The Sunday Reset", character: "dilo", weekNumber: 2,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "You wouldn't run a gaming PC for 7 days straight without a restart. Why do it to your brain? Sunday is for clearing the cache so Monday doesn't suck.",
        quote: "A RESET IS NOT QUITTING. IT IS MAKING SPACE TO START THE NEXT WEEK ON PURPOSE.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Perfect Reset Routine",
        steps: [
          "Design your ideal Sunday checklist:",
          "1. Body Recharge (e.g., Nap).",
          "2. Soul Recharge (e.g., Music).",
          "3. The Setup (Packing bag for Monday).",
        ],
        xpBoost: "Go to bed 30 mins early tonight. Put your phone in another room. Just recharge.",
        interactive: [
          { type: "text", id: "d7_body", prompt: "Body Recharge activity:", placeholder: "e.g., Nap, Stretch, Walk..." },
          { type: "text", id: "d7_soul", prompt: "Soul Recharge activity:", placeholder: "e.g., Music, Drawing, Nature..." },
          { type: "text", id: "d7_setup", prompt: "The Setup for Monday:", placeholder: "e.g., Pack bag, lay out clothes..." },
          { type: "checklist", id: "d7_early", prompt: "XP Boost:", options: ["Going to bed 30 mins early", "Phone in another room"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel burned out.",
        howToUse: "Stop everything. Execute your Reset Protocol.",
        yourTurn: "Create your 'Sunday Protocol'.",
        interactive: [
          { type: "text", id: "d7_protocol", prompt: "My Sunday Protocol:", placeholder: "Step by step..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Brain Dump",
        instructions: "Close your eyes. Imagine opening a valve in your ear. Let all thoughts pour out like water into a bucket. Your head is now empty and light.",
      },
      glitchPuzzle: {
        cheatCode: "REST IS NOT A REWARD. IT'S A HARDWARE REQUIREMENT.",
        puzzleTitle: "PUZZLE: The Unplugged Maze",
        puzzleContent: "Find the path to the charger without touching any screens.",
        interactive: [
          { type: "choice", id: "d7_maze", prompt: "Best way to unplug?", options: ["Go outside", "Read a book", "Take a nap", "All of the above"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  8: {
    day: 8, title: "Brain Hacks", character: "dilo", weekNumber: 3,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Highlighting alone is often not enough. Active recall adds the useful part: close the notes, try to remember, then check what you missed.",
        quote: "CLOSE THE NOTES. TRY TO REMEMBER. THEN CHECK WHAT YOU MISSED.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Cheat Sheet Method",
        steps: [
          "Pick a hard subject.",
          "Imagine you are allowed ONE index card for the test.",
          "Condense the entire chapter onto that box. Prioritize.",
        ],
        xpBoost: "Explain a complex topic to your dog (or a pillow). If the explanation gets stuck, you just found what to review next.",
        interactive: [
          { type: "text", id: "d8_subject", prompt: "Your hard subject:", placeholder: "e.g., Math, History..." },
          { type: "text", id: "d8_cheatsheet", prompt: "Your Cheat Sheet (3 key points):", placeholder: "1. ... 2. ... 3. ..." },
          { type: "checklist", id: "d8_explain", prompt: "XP Boost:", options: ["Explained a topic to a pet/pillow"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you have too much to learn.",
        howToUse: "Force yourself to summarize it in 3 bullet points.",
        yourTurn: "Create your Ultimate Cheat Sheet here.",
        interactive: [
          { type: "text", id: "d8_summary", prompt: "Summarize in 3 bullets:", placeholder: "• Point 1\n• Point 2\n• Point 3" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Focus Beam",
        instructions: "Look at one object for 60 seconds. Blink normally. When your attention wanders, notice it and gently bring it back.",
      },
      glitchPuzzle: {
        cheatCode: "RECALL IT. CHECK IT. CORRECT IT. TRY AGAIN.",
        puzzleTitle: "PUZZLE: Memory Matrix",
        puzzleContent: "Draw 9 symbols. Cover them. Draw them again from memory.",
        interactive: [
          { type: "drawing", id: "d8_memory", prompt: "Draw 9 symbols from memory:" },
          { type: "scramble", id: "d8_scramble", prompt: "Unscramble this brain hack:", word: "RECALL", scrambleHint: "It means to remember something from memory" },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  9: {
    day: 9, title: "The Time Ninja", character: "luli", weekNumber: 3,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Multitasking often means switching attention back and forth, which can make both tasks messier. Pick one target, work on it, then take a break. That's the Ninja way.",
        quote: "PICK ONE TARGET. GIVE IT YOUR ATTENTION. THEN CHOOSE THE NEXT.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Power Hour",
        steps: [
          "Plan your next hour:",
          "25 Mins: Pure Work.",
          "5 Mins: Pure Break.",
          "25 Mins: Pure Work.",
          "5 Mins: Victory Dance.",
        ],
        xpBoost: "Turn off non-essential notifications for 1 hour. Notice whether it feels easier to focus.",
        interactive: [
          { type: "text", id: "d9_task", prompt: "What will you work on?", placeholder: "Your focus task..." },
          { type: "checklist", id: "d9_pomodoro", prompt: "Power Hour checklist:", options: ["25 min work #1 done", "5 min break taken", "25 min work #2 done", "Victory dance completed"] },
          { type: "checklist", id: "d9_notifs", prompt: "XP Boost:", options: ["Turned off ALL notifications for 1 hour"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When a task feels huge.",
        howToUse: "Set a timer for 25 minutes. Do ONLY that task.",
        yourTurn: "Schedule your Power Hour.",
        interactive: [
          { type: "text", id: "d9_schedule", prompt: "My Power Hour schedule:", placeholder: "Time and task..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Time Expansion",
        instructions: "Sit still. Count 60 seconds in your head. Open your eyes when you think 1 minute has passed. Check the clock. Were you fast or slow?",
      },
      glitchPuzzle: {
        cheatCode: "WORK LIKE A SNIPER, NOT A MACHINE GUN. ONE TARGET AT A TIME.",
        puzzleTitle: "PUZZLE: The Time Paradox",
        puzzleContent: "5 machines make 5 widgets in 5 mins. How long for 100 machines to make 100 widgets?",
        interactive: [
          { type: "choice", id: "d9_puzzle", prompt: "The answer is:", options: ["5 minutes", "100 minutes", "500 minutes", "1 minute"] },
          { type: "matching", id: "d9_matching", prompt: "Match the time hack to its benefit:", pairs: [
            { left: "Pomodoro", right: "Deep focus bursts" },
            { left: "Time blocking", right: "Scheduled priorities" },
            { left: "2-minute rule", right: "Instant action" },
            { left: "Eisenhower matrix", right: "Urgent vs important" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  10: {
    day: 10, title: "The Procrastination Slayer", character: "dilo", weekNumber: 3,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Procrastination can come from overwhelm, boredom, uncertainty, fear, or simply not knowing where to start. A useful move is to make the first step tiny.",
        quote: "MAKE THE FIRST STEP SMALL ENOUGH TO START NOW.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The 5-Minute Glitch",
        steps: [
          "What are you avoiding?",
          "The Contract: 'I will work on this for exactly 5 minutes. Then I can stop.'",
          "Start the timer. Go.",
        ],
        xpBoost: "Prepare your desk for tomorrow. Open the book. Remove friction.",
        interactive: [
          { type: "text", id: "d10_avoiding", prompt: "What are you avoiding?", placeholder: "The thing you keep putting off..." },
          { type: "checklist", id: "d10_contract", prompt: "The 5-Minute Contract:", options: ["I commit to 5 minutes", "Timer started", "5 minutes completed"] },
          { type: "checklist", id: "d10_prep", prompt: "XP Boost:", options: ["Desk prepared for tomorrow"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you can't start.",
        howToUse: "Make the start small: just 5 minutes.",
        yourTurn: "Sign the 5-Minute Contract.",
        interactive: [
          { type: "text", id: "d10_sign", prompt: "I, ___, commit to starting for 5 minutes:", placeholder: "Type your name to sign..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Heavy Blanket",
        instructions: "Imagine a heavy blanket on your shoulders. It pushes down the frantic energy. You feel grounded. Slow. Calm.",
      },
      glitchPuzzle: {
        cheatCode: "MOTIVATION COMES AFTER YOU START MOVING.",
        puzzleTitle: "PUZZLE: Beat the Clock",
        puzzleContent: "Complete these micro-tasks before time runs out!",
        interactive: [
          { type: "drawing", id: "d10_tangram", prompt: "Draw a square using 5 shapes:" },
          { type: "timed", id: "d10_timed", prompt: "⚡ Speed Round: Anti-Procrastination!", timeLimit: 45, tasks: [
            { prompt: "Name one thing you're avoiding", type: "text" },
            { prompt: "Tap when you feel ready to start", type: "tap" },
            { prompt: "Write the first tiny step", type: "text" },
            { prompt: "Tap to commit to doing it NOW", type: "tap" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  11: {
    day: 11, title: "Project Manager Mode", character: "luli", weekNumber: 3,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "A big project is just a scary monster. If you try to eat it whole, you choke. Chop it into nuggets.",
        quote: "BIG PROJECTS GET SMALLER WHEN YOU TURN THEM INTO CLEAR NEXT STEPS.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Salami Slice",
        steps: [
          "Take a big deadline.",
          "Slice it into 5 tiny steps.",
          "Schedule only Step 1 for today.",
        ],
        xpBoost: "Check off one item from a list. Notice the small win.",
        interactive: [
          { type: "text", id: "d11_deadline", prompt: "Your big deadline:", placeholder: "e.g., Science project due Friday" },
          { type: "text", id: "d11_slice1", prompt: "Step 1:", placeholder: "Tiny first step..." },
          { type: "text", id: "d11_slice2", prompt: "Step 2:", placeholder: "Next small step..." },
          { type: "text", id: "d11_slice3", prompt: "Step 3:", placeholder: "..." },
          { type: "text", id: "d11_slice4", prompt: "Step 4:", placeholder: "..." },
          { type: "text", id: "d11_slice5", prompt: "Step 5:", placeholder: "Final step..." },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When a goal scares you.",
        howToUse: "Break it down until step 1 is laughably easy.",
        yourTurn: "Slice up your monster project.",
        interactive: [
          { type: "text", id: "d11_monster", prompt: "Your monster project sliced:", placeholder: "Break it down..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Step by Step",
        instructions: "Walk across the room in SUPER slow motion. Feel your heel touch the floor. Then the toes. You only need to take the next step.",
      },
      glitchPuzzle: {
        cheatCode: "HOW DO YOU EAT AN ELEPHANT? ONE BITE AT A TIME.",
        puzzleTitle: "PUZZLE: Tower of Hanoi",
        puzzleContent: "Move the stack one disk at a time. Never place a larger disk on a smaller one.",
        interactive: [
          { type: "choice", id: "d11_puzzle", prompt: "Minimum moves for 3 disks?", options: ["5 moves", "7 moves", "9 moves", "11 moves"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  12: {
    day: 12, title: "Bio-Hacking", character: "dilo", weekNumber: 4,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Mornings in a family house are usually a war zone. Bathroom hogging? Yelling? That drains your battery. Let's hack the morning server.",
        quote: "YOUR ROUTINES DO NOT HAVE TO BE PERFECT TO HELP YOU FEEL MORE READY.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Peace Treaty",
        steps: [
          "Identify the #1 cause of morning stress.",
          "THE FIX: Create a system tonight to prevent it.",
          "ANNOUNCE IT: 'I'm trying a new routine tomorrow.'",
        ],
        xpBoost: "Tomorrow, be the first to say 'Good morning' with a smile. Set the server difficulty to Easy.",
        interactive: [
          { type: "choice", id: "d12_stress", prompt: "Your #1 morning stress:", options: ["Bathroom fights", "Running late", "No clean clothes", "Can't wake up", "Family yelling"] },
          { type: "text", id: "d12_fix", prompt: "Your fix system:", placeholder: "Tonight I will..." },
          { type: "checklist", id: "d12_announce", prompt: "Actions:", options: ["Announced new routine", "Will say 'Good morning' first tomorrow"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When life feels chaotic.",
        howToUse: "Build a system. Remove friction the night before.",
        yourTurn: "Design your morning hack protocol.",
        interactive: [
          { type: "text", id: "d12_morning", prompt: "My morning hack:", placeholder: "Step by step morning routine..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Morning Sunlight",
        instructions: "Tomorrow: Stand by a window. Close your eyes. Let the sun hit your face. Feel the light waking up your cells.",
      },
      glitchPuzzle: {
        cheatCode: "PROTECT YOUR MORNINGS. IF YOU WIN THE MORNING, YOU WIN THE DAY.",
        puzzleTitle: "PUZZLE: Optical Illusion",
        puzzleContent: "Stare at the center of a spiral. Is it moving? (Your brain creates the illusion)",
        interactive: [
          { type: "choice", id: "d12_illusion", prompt: "Is your brain tricking you?", options: ["Yes, it seems to move!", "No, I see it's still", "I'm not sure"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  13: {
    day: 13, title: "The Focus Fortress", character: "luli", weekNumber: 4,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Your attention is currency. Apps are fighting to steal your wallet. Build a fortress so you decide where to spend it.",
        quote: "FOCUS GETS EASIER WHEN YOU MAKE DISTRACTIONS HARDER TO REACH.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: Notification Audit",
        steps: [
          "Go to your phone Settings.",
          "Turn off notifications for everything except VIPs.",
          "Games? Off. Instagram? Off.",
        ],
        xpBoost: "Unsubscribe from 3 YouTube channels you don't watch anymore. Declutter.",
        interactive: [
          { type: "checklist", id: "d13_audit", prompt: "Notification Audit:", options: ["Turned off game notifications", "Turned off social media notifications", "Only VIP contacts can notify me"] },
          { type: "checklist", id: "d13_unsub", prompt: "XP Boost:", options: ["Unsubscribed from channel #1", "Unsubscribed from channel #2", "Unsubscribed from channel #3"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel digital exhaustion.",
        howToUse: "Turn on 'Do Not Disturb'.",
        yourTurn: "Draw your Fortress. What do you protect? What do you block?",
        interactive: [
          { type: "drawing", id: "d13_fortress", prompt: "Draw your Focus Fortress:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Bell",
        instructions: "Listen to a sound fading away. Keep listening until you hear absolute silence. Stay in that silence for 10 seconds.",
      },
      glitchPuzzle: {
        cheatCode: "YOU ARE THE USER, NOT THE PRODUCT. DON'T LET THE ALGORITHM PROGRAM YOU.",
        puzzleTitle: "PUZZLE: The Stroop Effect",
        puzzleContent: "Read the COLORS, not the words: RED (in blue), BLUE (in green), GREEN (in red)",
        interactive: [
          { type: "choice", id: "d13_stroop", prompt: "Was it hard to read colors instead of words?", options: ["Very hard!", "A bit tricky", "Easy peasy", "My brain broke"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  14: {
    day: 14, title: "Celebration & Review", character: "dilo", weekNumber: 4,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Gamers look at stats to improve. Let's look at your stats for the week. Be honest, no judgment.",
        quote: "SMALL EFFORTS COUNT. REVIEW THEM, NOTICE WHAT WORKED, AND KEEP GOING.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Weekly Stat Sheet",
        steps: [
          "Review your week.",
          "High Score: Best moment?",
          "Damage Taken: What went wrong?",
          "New Strategy: One hack for next week.",
        ],
        xpBoost: "Reward yourself physically. Buy a treat. You survived Level 2.",
        interactive: [
          { type: "text", id: "d14_high", prompt: "High Score (best moment):", placeholder: "The best thing that happened..." },
          { type: "text", id: "d14_damage", prompt: "Damage Taken (what went wrong):", placeholder: "What didn't go as planned..." },
          { type: "text", id: "d14_strategy", prompt: "New Strategy for next week:", placeholder: "One hack I'll try..." },
          { type: "slider", id: "d14_rating", prompt: "Rate your week (1-10):", min: 1, max: 10 },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel like failing.",
        howToUse: "Look at your 'High Scores'. You are making progress.",
        yourTurn: "Fill in your stats. Give yourself a star rating.",
        interactive: [
          { type: "slider", id: "d14_stars", prompt: "Star rating for yourself:", min: 1, max: 5 },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Gratitude Scan",
        instructions: "Think of one thing that went right. Replay it like a movie clip. Feel the happiness again.",
      },
      glitchPuzzle: {
        cheatCode: "SMALL PROGRESS IS STILL PROGRESS. CELEBRATE THE WINS.",
        puzzleTitle: "PUZZLE: Sudoku (Mini)",
        puzzleContent: "Fill in the 4×4 grid so each row and column has 1, 2, 3, 4.",
        interactive: [
          { type: "choice", id: "d14_sudoku", prompt: "Did you solve it?", options: ["Solved it!", "Almost got it", "Need more practice"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  15: {
    day: 15, title: "Overload Button", character: "luli", weekNumber: 5,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Superheroes don't work alone. They have a team. Trying to do everything yourself leads to a crash. It is brave to say 'I am overloaded'.",
        quote: "YOU DO NOT HAVE TO DO EVERYTHING AT ONCE. CHOOSE WHAT MATTERS MOST NOW.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Family SOS",
        steps: [
          "Find a task you can DELEGATE.",
          "THE MISSION: Ask a family member for specific help.",
          "THE DEAL: Offer a trade later.",
        ],
        xpBoost: "Say 'No' to a request today if you are overloaded. 'I can't right now, I need to focus.'",
        interactive: [
          { type: "text", id: "d15_delegate", prompt: "Task to delegate:", placeholder: "What can someone else help with..." },
          { type: "text", id: "d15_trade", prompt: "What will you offer in return?", placeholder: "I'll trade..." },
          { type: "checklist", id: "d15_no", prompt: "XP Boost:", options: ["Said 'No' to something today"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you are drowning in tasks.",
        howToUse: "Delegate. Ask for help.",
        yourTurn: "Sort your chaos. Draw the Eisenhower Box.",
        interactive: [
          { type: "drawing", id: "d15_eisenhower", prompt: "Draw the Eisenhower Box (Urgent/Important grid):" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Box Breathing",
        instructions: "Inhale 4s. Hold 4s. Exhale 4s. Hold 4s. Repeat x4. System Reset.",
      },
      glitchPuzzle: {
        cheatCode: "IF IT'S NOT A 'HELL YES', IT'S A 'NO'.",
        puzzleTitle: "PUZZLE: Logic Riddle",
        puzzleContent: "I speak without a mouth. What am I?",
        interactive: [
          { type: "choice", id: "d15_riddle", prompt: "The answer is:", options: ["Echo", "Book", "Clock", "Shadow"] },
          { type: "matching", id: "d15_match", prompt: "Match each task to its priority level:", pairs: [
            { left: "Homework due tomorrow", right: "Urgent + Important" },
            { left: "Clean your room", right: "Not Urgent + Important" },
            { left: "Reply to a meme", right: "Not Urgent + Not Important" },
            { left: "Friend crying at school", right: "Urgent + Important" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  16: {
    day: 16, title: "Money Boss Level 1", character: "dilo", weekNumber: 5,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Money is energy tokens. You trade your life energy (time) for money. Before you buy shoes, ask: 'Is this worth 10 hours of my life?'",
        quote: "MONEY CHOICES GET CLEARER WHEN YOU KNOW WHAT IS COMING IN, GOING OUT, AND WHY.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Price of Cool",
        steps: [
          "Pick an item you want to buy.",
          "Find the price.",
          "Calculate your earnings per hour.",
          "Cost in Life Hours = Price ÷ Hourly Rate.",
          "Verdict: Worth it?",
        ],
        xpBoost: "Count the cash in your wallet right now. Awareness is power.",
        interactive: [
          { type: "text", id: "d16_item", prompt: "Item you want:", placeholder: "e.g., New shoes..." },
          { type: "text", id: "d16_price", prompt: "Price:", placeholder: "$..." },
          { type: "text", id: "d16_hourly", prompt: "Your earnings per hour:", placeholder: "$..." },
          { type: "text", id: "d16_hours", prompt: "Cost in life hours:", placeholder: "= ... hours of your life" },
          { type: "choice", id: "d16_verdict", prompt: "Verdict:", options: ["Worth it!", "Not worth it", "Need to think more", "Saving up instead"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "Before impulse buying.",
        howToUse: "Use the 'Time Cost' calculation. Wait 24h.",
        yourTurn: "Calculate the 'Time Cost' of 3 things.",
        interactive: [
          { type: "text", id: "d16_cost1", prompt: "Item 1 time cost:", placeholder: "Item → hours of life" },
          { type: "text", id: "d16_cost2", prompt: "Item 2 time cost:", placeholder: "Item → hours of life" },
          { type: "text", id: "d16_cost3", prompt: "Item 3 time cost:", placeholder: "Item → hours of life" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Enoughness",
        instructions: "Identify 5 things you own that you truly love. Touch them. Say 'Thank you'. Realize you already have so much.",
      },
      glitchPuzzle: {
        cheatCode: "BUY WITH A PLAN: KNOW WHAT YOU USE NOW, WHAT YOU OWE, AND WHAT CAN GROW IN VALUE.",
        puzzleTitle: "PUZZLE: The Missing Dollar",
        puzzleContent: "Three friends pay $30 for a room ($10 each). The manager gives $5 back. They each take $1, and $2 goes to the bellboy. They paid $27 + $2 = $29. Where is the missing dollar?",
        interactive: [
          { type: "text", id: "d16_dollar", prompt: "Where is the missing dollar?", placeholder: "The trick is..." },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  17: {
    day: 17, title: "The Budget Quest", character: "luli", weekNumber: 5,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Budgeting sounds boring. Call it 'Funds Allocation'. You are the CEO of You Inc. Where is the capital going?",
        quote: "A BUDGET IS A PLAN FOR YOUR MONEY, NOT A PUNISHMENT FOR SPENDING IT.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: Try a 50/30/20 Example",
        steps: [
          "Try this sample split on your next allowance. It is an example, not a rule — real needs and family situations differ.",
          "50% NEEDS (or responsibilities)",
          "30% WANTS",
          "20% DREAM FUND (The Big Goal).",
        ],
        xpBoost: "Put one coin into a physical 'Dream Fund' jar today.",
        interactive: [
          { type: "text", id: "d17_allowance", prompt: "Your allowance amount:", placeholder: "$..." },
          { type: "text", id: "d17_needs", prompt: "50% Needs ($):", placeholder: "What you need to spend on..." },
          { type: "text", id: "d17_wants", prompt: "30% Wants ($):", placeholder: "Fun stuff..." },
          { type: "text", id: "d17_dream", prompt: "20% Dream Fund ($):", placeholder: "Saving for..." },
          { type: "checklist", id: "d17_jar", prompt: "XP Boost:", options: ["Put a coin in the Dream Fund jar"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you get money.",
        howToUse: "Split it. Feed the Dream Fund first.",
        yourTurn: "Plan your budget. Draw 3 Jars.",
        interactive: [
          { type: "drawing", id: "d17_jars", prompt: "Draw your 3 Budget Jars:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Future Visualization",
        instructions: "Imagine yourself buying that Dream Item. Feel the pride that YOU bought it. Hold that feeling.",
      },
      glitchPuzzle: {
        cheatCode: "PAY YOURSELF FIRST. THE FUTURE YOU WILL THANK YOU.",
        puzzleTitle: "PUZZLE: Coin Triangle",
        puzzleContent: "Invert a triangle of 10 coins by moving only 3 coins.",
        interactive: [
          { type: "choice", id: "d17_coins", prompt: "Which coins do you move?", options: ["Corner coins", "Middle coins", "Edge coins", "Random coins"] },
          { type: "timed", id: "d17_timed", prompt: "⚡ Budget Speed Round! Categorize these fast:", timeLimit: 30, tasks: [
            { prompt: "New shoes = Need or Want?", type: "tap", answer: "Want" },
            { prompt: "School lunch = Need or Want?", type: "tap", answer: "Need" },
            { prompt: "Concert tickets = Need or Want?", type: "tap", answer: "Want" },
            { prompt: "Winter jacket = Need or Want?", type: "tap", answer: "Need" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  18: {
    day: 18, title: "Responsibility Audit", character: "dilo", weekNumber: 5,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Living in a messy glitch affects your mental RAM. But cleaning alone is boring. Let's turn it into a Co-Op Mission.",
        quote: "RESPONSIBILITY STARTS WITH THE NEXT THING YOU CAN ACTUALLY DO.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Speedrun Co-Op",
        steps: [
          "Challenge a sibling or family member.",
          "THE BET: Who cleans faster?",
          "GO: Set a timer. High energy music mandatory.",
        ],
        xpBoost: "Fix something in the house without telling anyone. Be the Silent Guardian.",
        interactive: [
          { type: "text", id: "d18_challenger", prompt: "Who are you challenging?", placeholder: "Name..." },
          { type: "text", id: "d18_area", prompt: "Area to clean:", placeholder: "Room, desk, closet..." },
          { type: "checklist", id: "d18_speedrun", prompt: "Speedrun:", options: ["Timer set", "Music on", "Cleaning done!", "Won the bet"] },
          { type: "checklist", id: "d18_guardian", prompt: "XP Boost:", options: ["Fixed something without telling anyone"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel lazy.",
        howToUse: "Gamify it. Speedrun the boring stuff.",
        yourTurn: "Log your speedrun stats.",
        interactive: [
          { type: "text", id: "d18_stats", prompt: "Speedrun time:", placeholder: "How fast did you finish?" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Clear Space",
        instructions: "Sit in your newly cleaned spot. Look at the clear floor. Notice how your breath feels easier. Enjoy the calm.",
      },
      glitchPuzzle: {
        cheatCode: "ENVIRONMENT DESIGN BEATS WILLPOWER.",
        puzzleTitle: "PUZZLE: Word Search",
        puzzleContent: "Find these words: CLEAN, ZEN, FOCUS",
        interactive: [
          { type: "checklist", id: "d18_words", prompt: "Words found:", options: ["CLEAN", "ZEN", "FOCUS"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  19: {
    day: 19, title: "Calendar Control", character: "luli", weekNumber: 6,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "If you don't plan your time, someone else will. Claim your territory.",
        quote: "PUT IMPORTANT THINGS ON THE CALENDAR BEFORE THE DAY FILLS ITSELF.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: Block the 'ME TIME'",
        steps: [
          "Take the weekly grid:",
          "Block out School.",
          "Block out 'ME TIME' (Gaming, Nothing). Make it official.",
          "Fit chores around that.",
        ],
        xpBoost: "Add your best friend's birthday to your calendar with a reminder.",
        interactive: [
          { type: "text", id: "d19_metime", prompt: "Your blocked ME TIME:", placeholder: "When and what..." },
          { type: "checklist", id: "d19_calendar", prompt: "Calendar actions:", options: ["School hours blocked", "ME TIME blocked", "Chores scheduled", "Best friend's birthday added"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you have no time.",
        howToUse: "Look at the calendar. Find the white space.",
        yourTurn: "Color-code your week. Claim your space.",
        interactive: [
          { type: "drawing", id: "d19_calendar_draw", prompt: "Draw your color-coded weekly calendar:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Pause Button",
        instructions: "Imagine a remote control. Press 'PAUSE'. Everything freezes. Take a breath. Press 'PLAY'.",
      },
      glitchPuzzle: {
        cheatCode: "A PLAN ISN'T A PRISON. IT'S A MAP TO FREEDOM.",
        puzzleTitle: "PUZZLE: Schedule Logic",
        puzzleContent: "Arrange 4 classes so that no boring subjects are back-to-back.",
        interactive: [
          { type: "choice", id: "d19_schedule", prompt: "Best scheduling strategy?", options: ["Alternate fun and boring", "All boring first", "All fun first", "Random order"] },
          { type: "scramble", id: "d19_scramble", prompt: "Unscramble this time-management word:", word: "CALENDAR", scrambleHint: "You use this to plan your days" },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  20: {
    day: 20, title: "The 'NO' Power", character: "dilo", weekNumber: 6,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "FOMO is a trap. JOMO (Joy Of Missing Out) is the upgrade. You don't have to be everywhere. Your energy is expensive.",
        quote: "A CLEAR NO CAN PROTECT YOUR TIME, ENERGY, AND BOUNDARIES.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Polite Decline",
        steps: [
          "Draft a text template for saying NO nicely.",
          "Template: 'Thanks for the invite! My social battery is at 0%, so I'm staying in tonight.'",
        ],
        xpBoost: "Skip one trend that everyone is talking about but you find boring.",
        interactive: [
          { type: "text", id: "d20_template1", prompt: "Your 'No' template #1:", placeholder: "Thanks but..." },
          { type: "text", id: "d20_template2", prompt: "Your 'No' template #2:", placeholder: "Another way to say no..." },
          { type: "text", id: "d20_template3", prompt: "Your 'No' template #3:", placeholder: "Yet another way..." },
          { type: "checklist", id: "d20_skip", prompt: "XP Boost:", options: ["Skipped a boring trend"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel pressured.",
        howToUse: "Use your script. Say no. Feel relief.",
        yourTurn: "Write 3 ways to say 'NO'.",
        interactive: [
          { type: "text", id: "d20_ways", prompt: "3 ways to say NO:", placeholder: "1... 2... 3..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Bubble",
        instructions: "Imagine a bubble around you. Say 'NO' to any thought trying to enter right now. Push it out gently.",
      },
      glitchPuzzle: {
        cheatCode: "PROTECT YOUR PEACE. YOUR ENERGY IS EXPENSIVE.",
        puzzleTitle: "PUZZLE: Impossible Object",
        puzzleContent: "Draw a Penrose Triangle — a shape that can't exist in real life!",
        interactive: [
          { type: "drawing", id: "d20_penrose", prompt: "Draw a Penrose Triangle:" },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  21: {
    day: 21, title: "Effectiveness Check", character: "luli", weekNumber: 6,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Pareto Principle: 20% of your actions give 80% of results. 20% of your friends give 80% of the fun. Stop doing the useless 80%.",
        quote: "BUSY IS NOT THE SAME AS EFFECTIVE. CHECK WHETHER YOUR EFFORT MATCHES THE GOAL.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Declutter",
        steps: [
          "Look at your desk.",
          "What is the 80% of stuff you never use?",
          "List 3 things you will throw out.",
        ],
        xpBoost: "Identify ONE subject in school that needs help. Spend 20 mins on it today.",
        interactive: [
          { type: "text", id: "d21_toss1", prompt: "Throwing out #1:", placeholder: "Item..." },
          { type: "text", id: "d21_toss2", prompt: "Throwing out #2:", placeholder: "Item..." },
          { type: "text", id: "d21_toss3", prompt: "Throwing out #3:", placeholder: "Item..." },
          { type: "text", id: "d21_subject", prompt: "Subject that needs help:", placeholder: "I'll spend 20 mins on..." },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel busy but stuck.",
        howToUse: "Ask: 'What is the ONE thing that matters?' Do that.",
        yourTurn: "Identify your 'Vital 20%'.",
        interactive: [
          { type: "text", id: "d21_vital", prompt: "My vital 20%:", placeholder: "The few things that really matter..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Letting Go",
        instructions: "Clench your fists tight. Hold. Imagine holding onto stress. Open hands suddenly. Let go.",
      },
      glitchPuzzle: {
        cheatCode: "DO LESS, BUT BETTER. EFFECTIVENESS > BUSYNESS.",
        puzzleTitle: "PUZZLE: Minimalist Puzzle",
        puzzleContent: "Remove 3 lines from this shape to make exactly 3 triangles.",
        interactive: [
          { type: "choice", id: "d21_puzzle", prompt: "How many triangles can you make?", options: ["1", "2", "3", "4"] },
          { type: "matching", id: "d21_match", prompt: "Match the concept to its meaning:", pairs: [
            { left: "Pareto Principle", right: "80/20 Rule" },
            { left: "Declutter", right: "Remove the useless 80%" },
            { left: "Vital Few", right: "The 20% that matters" },
            { left: "Effectiveness", right: "Doing the right things" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  22: {
    day: 22, title: "Talent Scout", character: "dilo", weekNumber: 6,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Sometimes it's hard to see your own label from inside the jar. You need an outside mirror.",
        quote: "YOU DO NOT HAVE TO KNOW YOUR WHOLE FUTURE. NOTICE WHAT YOU ENJOY, PRACTICE, AND WANT TO EXPLORE.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Talent Detective",
        steps: [
          "Interview 3 family members.",
          "QUESTION: 'What is one thing you think comes easily to me?'",
          "LISTEN: Write it down. Say 'Thanks.'",
        ],
        xpBoost: "Return the favor. Tell a sibling: 'You are really good at [X].'",
        interactive: [
          { type: "text", id: "d22_talent1", prompt: "Person 1 says your talent is:", placeholder: "Their answer..." },
          { type: "text", id: "d22_talent2", prompt: "Person 2 says your talent is:", placeholder: "Their answer..." },
          { type: "text", id: "d22_talent3", prompt: "Person 3 says your talent is:", placeholder: "Their answer..." },
          { type: "checklist", id: "d22_favor", prompt: "XP Boost:", options: ["Told someone they're good at something"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you are doubting your strengths or value.",
        howToUse: "Read the notes and look for concrete evidence of strengths, effort, kindness, or progress. If thoughts about having no value feel intense, persistent, or unsafe, tell a trusted adult and get support.",
        yourTurn: "Fill the Ikigai circles.",
        interactive: [
          { type: "drawing", id: "d22_ikigai", prompt: "Draw your Ikigai (What you love + Good at + World needs + Paid for):" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Heart Compass",
        instructions: "Place hand on heart. Ask: 'What makes me forget to check my phone?' Listen to the answer.",
      },
      glitchPuzzle: {
        cheatCode: "YOUR PASSION SHOULD BE YOUR COMPASS.",
        puzzleTitle: "PUZZLE: Career Decoder",
        puzzleContent: "Unscramble these future jobs: GNIREENIGNE, NGISED, ENICDEM",
        interactive: [
          { type: "text", id: "d22_job1", prompt: "GNIREENIGNE =", placeholder: "Unscrambled..." },
          { type: "text", id: "d22_job2", prompt: "NGISED =", placeholder: "Unscrambled..." },
          { type: "text", id: "d22_job3", prompt: "ENICDEM =", placeholder: "Unscrambled..." },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  23: {
    day: 23, title: "The Dream Board", character: "luli", weekNumber: 6,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "A vision board does not predict the future. It helps you explore what you want to move toward. Let's sketch a Level 100 direction and choose one step that fits it.",
        quote: "IF YOU CAN PICTURE A DIRECTION, YOU CAN START CHOOSING STEPS TOWARD IT.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Vision Page",
        steps: [
          "Fill the next page with drawings or words.",
          "Prompt: Where do you live? Who are you with?",
          "Rule: No logic allowed. Just vibes.",
        ],
        xpBoost: "Take a pic of your board and make it your wallpaper.",
        interactive: [
          { type: "text", id: "d23_live", prompt: "Where do you live at Level 100?", placeholder: "Dream location..." },
          { type: "text", id: "d23_with", prompt: "Who are you with?", placeholder: "Dream squad..." },
          { type: "text", id: "d23_doing", prompt: "What are you doing?", placeholder: "Dream career/life..." },
          { type: "checklist", id: "d23_wallpaper", prompt: "XP Boost:", options: ["Made dream board my wallpaper"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you lose motivation.",
        howToUse: "Look at your Vision Board. Remember WHY.",
        yourTurn: "Create your Vision Board. Go wild.",
        interactive: [
          { type: "drawing", id: "d23_vision", prompt: "Draw your Vision Board:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Time Travel",
        instructions: "Imagine you are 25 years old. You are waking up in your dream house. What do you see? Stay there for 1 minute.",
      },
      glitchPuzzle: {
        cheatCode: "YOUR MIND MOVES TOWARDS WHAT IT FOCUSES ON.",
        puzzleTitle: "PUZZLE: Visual Puzzle",
        puzzleContent: "Find the hidden star in the pattern.",
        interactive: [
          { type: "choice", id: "d23_star", prompt: "Where was the star hidden?", options: ["Top left", "Center", "Bottom right", "It was everywhere!"] },
          { type: "timed", id: "d23_timed", prompt: "⚡ Vision Board Speed Round! Answer fast:", timeLimit: 25, tasks: [
            { prompt: "Dream job in 3 words?", type: "text" },
            { prompt: "Dream city to live in?", type: "text" },
            { prompt: "One thing on your bucket list?", type: "text" },
            { prompt: "Your life motto?", type: "text" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  24: {
    day: 24, title: "Goal Setting Sniper", character: "dilo", weekNumber: 6,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "'I want to get better at math' is a wish. 'I want to get a B+ by June' is a PLAN.",
        quote: "A GOAL GETS STRONGER WHEN YOU CAN NAME THE NEXT STEP AND THE DEADLINE.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The SMART Goal",
        steps: [
          "Pick one goal.",
          "Make it SMART: Specific, Measurable, Achievable, Relevant, Time-bound.",
        ],
        xpBoost: "Tell one person your goal today. Accountability.",
        interactive: [
          { type: "text", id: "d24_goal", prompt: "Your goal:", placeholder: "I want to..." },
          { type: "text", id: "d24_specific", prompt: "Specific:", placeholder: "Exactly what..." },
          { type: "text", id: "d24_measurable", prompt: "Measurable:", placeholder: "How will you know..." },
          { type: "text", id: "d24_deadline", prompt: "Time-bound:", placeholder: "By when..." },
          { type: "checklist", id: "d24_told", prompt: "XP Boost:", options: ["Told someone my goal"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When a goal feels vague.",
        howToUse: "Put a date on it.",
        yourTurn: "Write your SMART goal.",
        interactive: [
          { type: "text", id: "d24_smart", prompt: "My SMART goal:", placeholder: "Full SMART goal statement..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Laser Focus",
        instructions: "Imagine your goal is a target. You are an archer. Aim. Release. Bullseye.",
      },
      glitchPuzzle: {
        cheatCode: "A GOAL WITHOUT A DEADLINE IS JUST A DREAM.",
        puzzleTitle: "PUZZLE: The Maze",
        puzzleContent: "Find your way to the center of the maze.",
        interactive: [
          { type: "choice", id: "d24_maze", prompt: "What's the best maze strategy?", options: ["Follow the right wall", "Go straight always", "Random turns", "Use a map"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  25: {
    day: 25, title: "Failure is Just Data", character: "luli", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "In games, when you die, you respawn and try again with new knowledge. Failure isn't 'Game Over'. It's just 'Try Again'.",
        quote: "A MISTAKE CAN GIVE YOU USEFUL INFORMATION FOR THE NEXT ATTEMPT.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Fail Resume",
        steps: [
          "List 3 failures.",
          "Write: 'XP Gained / What I learned.'",
        ],
        xpBoost: "Share a funny 'fail story' with a friend. Laughing at it takes away its power.",
        interactive: [
          { type: "text", id: "d25_fail1", prompt: "Fail #1:", placeholder: "What happened..." },
          { type: "text", id: "d25_xp1", prompt: "XP Gained from fail #1:", placeholder: "What I learned..." },
          { type: "text", id: "d25_fail2", prompt: "Fail #2:", placeholder: "What happened..." },
          { type: "text", id: "d25_xp2", prompt: "XP Gained from fail #2:", placeholder: "What I learned..." },
          { type: "text", id: "d25_fail3", prompt: "Fail #3:", placeholder: "What happened..." },
          { type: "text", id: "d25_xp3", prompt: "XP Gained from fail #3:", placeholder: "What I learned..." },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you mess up.",
        howToUse: "Ask: 'What XP did I gain?'",
        yourTurn: "Fill your Fail Resume.",
        interactive: [
          { type: "text", id: "d25_resume", prompt: "My Fail → XP table:", placeholder: "Fail: ... XP: ..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Shake Off",
        instructions: "Stand up. Shake your hands. Shake your legs. Shake your whole body like a wet dog. Shake off the shame. Stop. Feel the energy.",
      },
      glitchPuzzle: {
        cheatCode: "WIN OR LEARN. YOU NEVER LOSE.",
        puzzleTitle: "PUZZLE: Lateral Thinking",
        puzzleContent: "In Monopoly, if you land on 'Go to Jail', do you collect $200?",
        interactive: [
          { type: "choice", id: "d25_monopoly", prompt: "Do you collect $200?", options: ["Yes", "No", "Only on Tuesdays", "Depends on the dice"] },
          { type: "scramble", id: "d25_scramble", prompt: "Unscramble this resilience word:", word: "RESPAWN", scrambleHint: "What gamers do after failing" },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  26: {
    day: 26, title: "Networking & Mentors", character: "dilo", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Adults and mentors around you have solved problems you have not met yet. You do not need to copy their lives — but you can borrow useful questions, lessons, and strategies.",
        quote: "YOU CAN LEARN FASTER WHEN YOU ASK GOOD QUESTIONS AND LISTEN TO PEOPLE WITH EXPERIENCE.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Origin Story",
        steps: [
          "Ask a parent, caregiver, teacher, coach, or other trusted adult for a short 'Coffee Chat'.",
          "'What was your first job?'",
          "'Best financial decision?'",
          "'What do you wish you knew at 13?'",
        ],
        xpBoost: "Identify a trusted mentor or role model. Ask one useful question — with a parent/caregiver involved when appropriate.",
        interactive: [
          { type: "text", id: "d26_firstjob", prompt: "Their first job:", placeholder: "..." },
          { type: "text", id: "d26_bestdecision", prompt: "Best financial decision:", placeholder: "..." },
          { type: "text", id: "d26_wish", prompt: "What they wish they knew at 13:", placeholder: "..." },
          { type: "text", id: "d26_mentor", prompt: "Who is your mentor?", placeholder: "Name and why..." },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you are stuck.",
        howToUse: "Ask someone who beat this level.",
        yourTurn: "Profile your Mentor. Extract wisdom.",
        interactive: [
          { type: "text", id: "d26_profile", prompt: "Mentor profile:", placeholder: "Name, skills, wisdom..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Empty Chair",
        instructions: "Imagine a room. Opposite you sits a trusted role model. What question would you ask? Write the advice you think fits their real, known approach — then label it as your own guess unless they actually said it.",
      },
      glitchPuzzle: {
        cheatCode: "SUCCESS LEAVES CLUES. COPY THE STRATEGY.",
        puzzleTitle: "PUZZLE: Connection Riddle",
        puzzleContent: "What connects: Swiss, Cottage, Cake?",
        interactive: [
          { type: "choice", id: "d26_riddle", prompt: "The connection is:", options: ["Cheese", "House", "Sweet", "Mountain"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  27: {
    day: 27, title: "Impact Maker", character: "luli", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Confidence comes from competence, but mostly from CONTRIBUTION. When you help the team, you feel valuable.",
        quote: "IMPACT CAN START SMALL: HELP ONE PERSON, SOLVE ONE PROBLEM, SHARE ONE USEFUL THING.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Ninja Service",
        steps: [
          "Perform a 'Stealth Kindness Mission'.",
          "Ideas: Make coffee for parents. Fold laundry.",
          "RULE: Do not get caught.",
        ],
        xpBoost: "Write a sticky note: 'I love that you [X]'. Stick it on the mirror.",
        interactive: [
          { type: "text", id: "d27_mission", prompt: "Your stealth mission:", placeholder: "What will you do secretly..." },
          { type: "checklist", id: "d27_stealth", prompt: "Stealth status:", options: ["Mission completed", "Did NOT get caught", "Wrote a sticky note"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel sad.",
        howToUse: "Do something for someone else. Action cures fear.",
        yourTurn: "Design your Stealth Mission.",
        interactive: [
          { type: "text", id: "d27_design", prompt: "Mission plan:", placeholder: "Target, action, escape route..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Expanding Heart",
        instructions: "Imagine a warm light in your chest. Expand it to fill the room, the house, the world. Send good vibes.",
      },
      glitchPuzzle: {
        cheatCode: "TO FEEL IMPORTANT, MAKE SOMEONE ELSE FEEL IMPORTANT.",
        puzzleTitle: "PUZZLE: The Bridge",
        puzzleContent: "4 people cross a bridge at night with one flashlight. They can only cross in pairs. Times: 1min, 2min, 5min, 10min.",
        interactive: [
          { type: "choice", id: "d27_bridge", prompt: "Fastest total crossing time?", options: ["17 minutes", "19 minutes", "21 minutes", "15 minutes"] },
          { type: "matching", id: "d27_match", prompt: "Match the kindness action to its effect:", pairs: [
            { left: "Make coffee for parents", right: "Shows appreciation" },
            { left: "Fold someone's laundry", right: "Eases their burden" },
            { left: "Write a sticky note", right: "Brightens their day" },
            { left: "Listen without advice", right: "Makes them feel heard" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  28: {
    day: 28, title: "The Legacy", character: "dilo", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "People won't remember your grades or your shoes. They will remember how you made them feel. That is your legacy.",
        quote: "BECOME THE KIND OF PERSON YOU WOULD BE PROUD TO BE REMEMBERED AS.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Eulogy of Cool",
        steps: [
          "Write 3 words you want people to use to describe you.",
          "Are you acting like that person today?",
        ],
        xpBoost: "Act like your 'Ideal Self' for just 1 hour today.",
        interactive: [
          { type: "text", id: "d28_word1", prompt: "Word #1:", placeholder: "e.g., Funny" },
          { type: "text", id: "d28_word2", prompt: "Word #2:", placeholder: "e.g., Kind" },
          { type: "text", id: "d28_word3", prompt: "Word #3:", placeholder: "e.g., Fearless" },
          { type: "choice", id: "d28_acting", prompt: "Are you acting like that person today?", options: ["Yes, mostly!", "Getting there", "Not yet, but I will", "Need to work on it"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "Before doing something risky.",
        howToUse: "Ask: 'Is this who I want to be?'",
        yourTurn: "Tag the Graffiti Wall with your Legacy Words.",
        interactive: [
          { type: "drawing", id: "d28_graffiti", prompt: "Design your Legacy Graffiti Wall:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Statue",
        instructions: "Sit perfectly still like a statue of a hero. Feel the dignity in your spine. You are solid.",
      },
      glitchPuzzle: {
        cheatCode: "CHARACTER IS WHO YOU ARE WHEN NO ONE IS LOOKING.",
        puzzleTitle: "PUZZLE: Cryptogram",
        puzzleContent: "Decode: Y.O.U. A.R.E. T.H.E. F.U.T.U.R.E.",
        interactive: [
          { type: "text", id: "d28_crypto", prompt: "What does it spell?", placeholder: "The decoded message..." },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  29: {
    day: 29, title: "The Gratitude Algorithm", character: "luli", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Luli CONNECTING...]",
        message: "Gratitude is not about pretending everything is great. It is a way to notice real good moments alongside the hard ones.",
        quote: "NOTICE WHAT IS GOOD WITHOUT PRETENDING THE HARD STUFF ISN'T THERE.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Top 10 High-Lights",
        steps: [
          "List 10 awesome things from this month.",
          "Big or tiny. Write them down to lock them in memory.",
        ],
        xpBoost: "Say 'Thank you' to someone who usually doesn't hear it.",
        interactive: [
          { type: "text", id: "d29_h1", prompt: "Highlight #1:", placeholder: "..." },
          { type: "text", id: "d29_h2", prompt: "Highlight #2:", placeholder: "..." },
          { type: "text", id: "d29_h3", prompt: "Highlight #3:", placeholder: "..." },
          { type: "text", id: "d29_h4", prompt: "Highlight #4:", placeholder: "..." },
          { type: "text", id: "d29_h5", prompt: "Highlight #5:", placeholder: "..." },
          { type: "text", id: "d29_h6", prompt: "Highlights #6-10:", placeholder: "6... 7... 8... 9... 10..." },
          { type: "checklist", id: "d29_thanks", prompt: "XP Boost:", options: ["Thanked someone unexpected"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel jealous.",
        howToUse: "Name 3 things you have right now.",
        yourTurn: "Draw a 'Top 10' Chart.",
        interactive: [
          { type: "drawing", id: "d29_chart", prompt: "Draw your Top 10 Chart:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: Savoring",
        instructions: "Think of one good moment from this month. Replay the sights, sounds, smells, tastes, or feelings you remember. Notice it without pretending the hard moments did not happen.",
      },
      glitchPuzzle: {
        cheatCode: "IT IS GRATEFUL PEOPLE WHO ARE HAPPY.",
        puzzleTitle: "PUZZLE: Happy Logic",
        puzzleContent: "Find the pattern: 😊 😊 😐 😊 😊 😐 😊 😊 ?",
        interactive: [
          { type: "choice", id: "d29_pattern", prompt: "What comes next?", options: ["😐", "😊", "😢", "🎉"] },
          { type: "timed", id: "d29_timed", prompt: "⚡ Gratitude Speed Round! Name these fast:", timeLimit: 20, tasks: [
            { prompt: "One person you're grateful for?", type: "text" },
            { prompt: "One food you love?", type: "text" },
            { prompt: "One place that makes you happy?", type: "text" },
            { prompt: "One skill you're proud of?", type: "text" },
          ]},
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  30: {
    day: 30, title: "The Epic Journey Review", character: "dilo", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Dilo CONNECTING...]",
        message: "Look at your XP bar. You leveled up. You are not the same person who started Day 1.",
        quote: "LOOK BACK. NAME WHAT CHANGED. KEEP THE NEXT STEP SMALL.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Before & After",
        steps: [
          "Flip back to Day 1.",
          "What is the biggest change in your mindset?",
          "Draw your Avatar NOW vs. THEN.",
        ],
        xpBoost: "Flip through all your entries fast. Watch your progress fly by.",
        interactive: [
          { type: "text", id: "d30_change", prompt: "Biggest mindset change:", placeholder: "I used to think... now I think..." },
          { type: "drawing", id: "d30_avatar", prompt: "Draw your Avatar: THEN vs NOW:" },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you feel stuck.",
        howToUse: "Look back at how far you have come.",
        yourTurn: "Draw your evolution.",
        interactive: [
          { type: "drawing", id: "d30_evolution", prompt: "Draw your evolution journey:" },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Mountain Top",
        instructions: "Imagine you have climbed a huge mountain. Look down at the path you walked. You made it.",
      },
      glitchPuzzle: {
        cheatCode: "PROGRESS IS SLOW, THEN SUDDEN. KEEP GOING.",
        puzzleTitle: "PUZZLE: The End",
        puzzleContent: "A riddle that leads back to Page 1: Where does every journey begin?",
        interactive: [
          { type: "choice", id: "d30_riddle", prompt: "Where does every journey begin?", options: ["With a single step", "At the beginning", "In your mind", "All of the above"] },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
  31: {
    day: 31, title: "The Unstoppable Contract", character: "dilo", weekNumber: 7,
    sections: {
      intro: {
        characterConnecting: "[Team CONNECTING...]",
        message: "This book ends, but the game continues. You have the tools. You have the codes. You are ready.",
        quote: "YOUR NEXT CHAPTER DOES NOT NEED A PERFECT PLAN. IT NEEDS A DIRECTION AND A FIRST STEP.",
        quoteAuthor: "Project Unstoppable",
      },
      briefing: {
        questTitle: "MAIN QUEST: The Signing Ceremony",
        steps: [
          "Read your Contract out loud.",
          "THE TWIST: Ask one family member to sign as a 'WITNESS'.",
          "Tell them: 'You are on my team.'",
        ],
        xpBoost: "Take a photo of you + your Witness + The Contract.",
        interactive: [
          { type: "text", id: "d31_contract", prompt: "I, ___, commit to being UNSTOPPABLE:", placeholder: "Write your contract pledge..." },
          { type: "text", id: "d31_witness", prompt: "Witness name:", placeholder: "Who signed as witness..." },
          { type: "checklist", id: "d31_ceremony", prompt: "Ceremony:", options: ["Read contract out loud", "Got a witness signature", "Took a photo together"] },
        ],
      },
      workbench: {
        toolTitle: "TOOL FOR LIFE (RESCUE KIT)",
        whenToUse: "When you want to give up.",
        howToUse: "Look at the signature. You made a promise.",
        yourTurn: "Sign the Contract. Make it official.",
        interactive: [
          { type: "text", id: "d31_sign", prompt: "Your signature:", placeholder: "Type your full name to sign..." },
        ],
      },
      systemReboot: {
        title: "MINDFULNESS: The Launch",
        instructions: "Count down from 10 to 1. 10... 9... 8... 7... 6... 5... 4... 3... 2... 1... Blast off! Open your eyes. You are ready.",
      },
      glitchPuzzle: {
        cheatCode: "YOU ARE UNSTOPPABLE.",
        puzzleTitle: "PUZZLE: The Final Key",
        puzzleContent: "What does this key open?",
        interactive: [
          { type: "text", id: "d31_key", prompt: "This key opens:", placeholder: "Your answer..." },
          { type: "scramble", id: "d31_scramble", prompt: "Unscramble the final word — your new title:", word: "UNSTOPPABLE", scrambleHint: "What you've become after 31 days" },
        ],
      },
      freeRoam: { title: "NOTES / DOODLES / BRAIN DUMP" },
    },
  },
};

// First-Aid Kit reference
export const firstAidKit = [
  { problem: "OVERWHELMED?", day: 1, action: "Close eyes. Visit Safe Server." },
  { problem: "SCARED?", day: 3, action: "Name the feeling." },
  { problem: "LEFT OUT?", day: 4, action: "Text a 'Center Circle' friend." },
  { problem: "HATED ON?", day: 5, action: "Be a Grey Rock." },
  { problem: "NAGGED?", day: 6, action: "Say: 'I hear you.'" },
  { problem: "TIRED?", day: 7, action: "Sleep. Reboot." },
  { problem: "CAN'T STUDY?", day: 8, action: "Make a Cheat Sheet." },
  { problem: "TOO MUCH HOMEWORK?", day: 9, action: "25 Mins Timer." },
  { problem: "PROCRASTINATING?", day: 10, action: "Just 5 Minutes." },
  { problem: "IMPULSE BUYING?", day: 16, action: "Wait 24 Hours." },
  { problem: "FEELING LAZY?", day: 18, action: "Speedrun with music." },
  { problem: "NO FREE TIME?", day: 19, action: "Block ME TIME first." },
  { problem: "DOUBTING YOURSELF?", day: 22, action: "Check your evidence of strengths." },
  { problem: "MESSED UP?", day: 25, action: "Check XP Gained." },
];

export const bonusContent = {
  quotes: [
    "YOU DO NOT NEED TO BECOME SOMEONE ELSE TO START BUILDING A STRONGER VERSION OF YOU.",
    "A TRAIT CAN FEEL LIKE A BUG IN ONE SITUATION AND BECOME A STRENGTH IN ANOTHER.",
    "FEELINGS ARE SIGNALS TO NOTICE, NOT LABELS THAT DEFINE YOU.",
    "PAY ATTENTION TO WHO HELPS YOU FEEL SAFE, RESPECTED, AND MORE LIKE YOURSELF.",
    "SOMEONE ELSE'S PUT-DOWN DOES NOT GET TO DECIDE YOUR VALUE.",
    "GOOD COMMUNICATION STARTS WITH SAYING WHAT YOU MEAN AND LISTENING FOR WHAT THE OTHER PERSON MEANS.",
    "A RESET IS NOT QUITTING. IT IS MAKING SPACE TO START THE NEXT WEEK ON PURPOSE.",
    "CLOSE THE NOTES. TRY TO REMEMBER. THEN CHECK WHAT YOU MISSED.",
    "PICK ONE TARGET. GIVE IT YOUR ATTENTION. THEN CHOOSE THE NEXT.",
    "MAKE THE FIRST STEP SMALL ENOUGH TO START NOW.",
    "BIG PROJECTS GET SMALLER WHEN YOU TURN THEM INTO CLEAR NEXT STEPS.",
    "YOUR ROUTINES DO NOT HAVE TO BE PERFECT TO HELP YOU FEEL MORE READY.",
    "FOCUS GETS EASIER WHEN YOU MAKE DISTRACTIONS HARDER TO REACH.",
    "SMALL EFFORTS COUNT. REVIEW THEM, NOTICE WHAT WORKED, AND KEEP GOING.",
    "YOU DO NOT HAVE TO DO EVERYTHING AT ONCE. CHOOSE WHAT MATTERS MOST NOW.",
    "MONEY CHOICES GET CLEARER WHEN YOU KNOW WHAT IS COMING IN, GOING OUT, AND WHY.",
    "A BUDGET IS A PLAN FOR YOUR MONEY, NOT A PUNISHMENT FOR SPENDING IT.",
    "RESPONSIBILITY STARTS WITH THE NEXT THING YOU CAN ACTUALLY DO.",
    "PUT IMPORTANT THINGS ON THE CALENDAR BEFORE THE DAY FILLS ITSELF.",
    "A CLEAR NO CAN PROTECT YOUR TIME, ENERGY, AND BOUNDARIES.",
    "BUSY IS NOT THE SAME AS EFFECTIVE. CHECK WHETHER YOUR EFFORT MATCHES THE GOAL.",
    "YOU DO NOT HAVE TO KNOW YOUR WHOLE FUTURE. NOTICE WHAT YOU ENJOY, PRACTICE, AND WANT TO EXPLORE.",
    "IF YOU CAN PICTURE A DIRECTION, YOU CAN START CHOOSING STEPS TOWARD IT.",
    "A GOAL GETS STRONGER WHEN YOU CAN NAME THE NEXT STEP AND THE DEADLINE.",
    "A MISTAKE CAN GIVE YOU USEFUL INFORMATION FOR THE NEXT ATTEMPT.",
    "YOU CAN LEARN FASTER WHEN YOU ASK GOOD QUESTIONS AND LISTEN TO PEOPLE WITH EXPERIENCE.",
    "IMPACT CAN START SMALL: HELP ONE PERSON, SOLVE ONE PROBLEM, SHARE ONE USEFUL THING.",
    "BECOME THE KIND OF PERSON YOU WOULD BE PROUD TO BE REMEMBERED AS.",
    "NOTICE WHAT IS GOOD WITHOUT PRETENDING THE HARD STUFF ISN'T THERE.",
    "LOOK BACK. NAME WHAT CHANGED. KEEP THE NEXT STEP SMALL.",
    "YOUR NEXT CHAPTER DOES NOT NEED A PERFECT PLAN. IT NEEDS A DIRECTION AND A FIRST STEP.",
  ],
};
