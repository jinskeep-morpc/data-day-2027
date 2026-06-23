## DATA DAY 2027 — "FIVE YEARS FORWARD" PALETTE

CORE
Momentum Teal    #008980   hero / primary
Path Indigo      #4455AE   secondary
Open Sky         #0C80AC   secondary
Velocity Orange  #FF6A3D   energetic accent
Ink              #15191F   text (near-black)
Slate            #71777D   mid neutral
Cloud            #F7FBFC   light surface

DATA-VIZ (categorical, color-blind-safe)
#0DA89F  #FF6A3D  #4455AE  #E0A21A  #B5519E  #4FB6DD

SCALES (50→900)
Teal     E9FBF9 D5F2EF AEE6DF 7DCFC6 4DB9AF 23A298 008980 007068 00564F 003B36
Indigo   F0F6FF E0EAFF C5D6FF A2B9FF 859DFF 6E84EB 586CCE 4455AE 323F89 202963
Sky      EAFAFF D5F0FF B0E1FC 80C8EE 53B0DD 3199C7 0C80AC 006890 004F70 003650
Velocity FFEEE4 FFDCCC FFBCA0 FF9873 FF7E53 FF6A3D D54E1E AF3807 842400 5B1100
Slate    F6F7F8 E9EBED D6D9DD B9BEC4 9FA5AC 888E95 71777D 5A6065 44484D 2D3134

# CSS

:root {
  /* Core */
  --dd-teal: #008980;        /* hero / primary */
  --dd-indigo: #4455AE;      /* secondary */
  --dd-sky: #0C80AC;         /* secondary */
  --dd-velocity: #FF6A3D;    /* energetic accent */
  --dd-ink: #15191F;         /* text */
  --dd-slate: #71777D;       /* mid neutral */
  --dd-cloud: #F7FBFC;       /* surface */

  /* Teal */
  --dd-teal-50:#E9FBF9; --dd-teal-100:#D5F2EF; --dd-teal-200:#AEE6DF; --dd-teal-300:#7DCFC6; --dd-teal-400:#4DB9AF;
  --dd-teal-500:#23A298; --dd-teal-600:#008980; --dd-teal-700:#007068; --dd-teal-800:#00564F; --dd-teal-900:#003B36;

  /* Indigo */
  --dd-indigo-50:#F0F6FF; --dd-indigo-100:#E0EAFF; --dd-indigo-200:#C5D6FF; --dd-indigo-300:#A2B9FF; --dd-indigo-400:#859DFF;
  --dd-indigo-500:#6E84EB; --dd-indigo-600:#586CCE; --dd-indigo-700:#4455AE; --dd-indigo-800:#323F89; --dd-indigo-900:#202963;

  /* Sky */
  --dd-sky-50:#EAFAFF; --dd-sky-100:#D5F0FF; --dd-sky-200:#B0E1FC; --dd-sky-300:#80C8EE; --dd-sky-400:#53B0DD;
  --dd-sky-500:#3199C7; --dd-sky-600:#0C80AC; --dd-sky-700:#006890; --dd-sky-800:#004F70; --dd-sky-900:#003650;

  /* Velocity Orange */
  --dd-velocity-50:#FFEEE4; --dd-velocity-100:#FFDCCC; --dd-velocity-200:#FFBCA0; --dd-velocity-300:#FF9873; --dd-velocity-400:#FF7E53;
  --dd-velocity-500:#FF6A3D; --dd-velocity-600:#D54E1E; --dd-velocity-700:#AF3807; --dd-velocity-800:#842400; --dd-velocity-900:#5B1100;

  /* Slate */
  --dd-slate-50:#F6F7F8; --dd-slate-100:#E9EBED; --dd-slate-200:#D6D9DD; --dd-slate-300:#B9BEC4; --dd-slate-400:#9FA5AC;
  --dd-slate-500:#888E95; --dd-slate-600:#71777D; --dd-slate-700:#5A6065; --dd-slate-800:#44484D; --dd-slate-900:#2D3134;

  /* Data-viz categorical */
  --dd-cat-1:#0DA89F; --dd-cat-2:#FF6A3D; --dd-cat-3:#4455AE; --dd-cat-4:#E0A21A; --dd-cat-5:#B5519E; --dd-cat-6:#4FB6DD;
}