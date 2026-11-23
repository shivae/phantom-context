"""Text banks for synthetic law-firm phone-assistant transcripts.

Everything here is fictional: firms, people, numbers, and policies. The banks
are combinatorial (templates x slot values) so transcripts vary across
scenarios, but they are still synthetic. See README "Limits".
"""

FIRST = [
    "Maria", "James", "Aisha", "Daniel", "Priya", "Marcus", "Elena", "Tyrone",
    "Sofia", "Kevin", "Mei", "Robert", "Fatima", "Luis", "Hannah", "Andre",
    "Grace", "Omar", "Natalie", "Victor", "Keisha", "Samuel", "Rosa", "Brian",
    "Yuki", "Carlos", "Leah", "Ibrahim", "Megan", "Dmitri",
]
LAST = [
    "Alvarez", "Thompson", "Okafor", "Nguyen", "Patel", "Robinson", "Kowalski",
    "Haddad", "Brennan", "Castillo", "Murphy", "Fischer", "Delgado",
    "Washington", "Sato", "Morales", "Becker", "Lindqvist", "Adeyemi", "Romano",
    "Chen", "Hughes", "Petrov", "Silva", "Gallagher", "Mensah", "Novak",
    "Reyes", "Abbott", "Ferreira",
]
ATTORNEYS = [
    "Dana Whitfield", "Rafael Ortega", "Lauren Cho", "Michael Esposito",
    "Simone Baptiste", "Gregory Hale", "Anita Raman", "Thomas Wexler",
]
PARALEGALS = ["Jordan Pike", "Casey Moreno", "Riley Grant", "Alex Duarte", "Morgan Lee", "Taylor Brooks"]
FIRMS = [
    "Harbor & Vale LLP", "Calder Pierce Law Group", "Northgate Trial Attorneys",
    "Meridian Legal Partners", "Ashford & Lune", "Redwood Advocacy Group",
    "Bellmont & Price", "Sterling Ridge Law", "Ostrander Kim LLP", "Lakeshore Legal Group",
]
CITIES = ["Sacramento", "Fresno", "Tucson", "Albuquerque", "Columbus", "Raleigh", "Tampa", "Boise", "Spokane", "Richmond"]
STREETS = ["Market Street", "Oak Avenue", "Fifth Street", "Riverside Drive", "Main Street", "Capitol Mall", "Elm Street", "Park Boulevard"]
ASSISTANT_NAMES = ["Avery", "Jamie", "Quinn", "Rowan", "Skyler", "Emery"]

PRACTICES = {
    "personal injury": {
        "matters": ["auto accident", "slip and fall", "dog bite", "bicycle collision", "rideshare accident", "trucking collision"],
        "fee": "a 33 percent contingency fee, or 40 percent if the case goes to trial",
        "fee_short": "the 33 percent contingency",
    },
    "employment": {
        "matters": ["wrongful termination", "unpaid overtime", "workplace retaliation", "disability discrimination"],
        "fee": "a 35 percent contingency fee",
        "fee_short": "the 35 percent contingency",
    },
    "workers' compensation": {
        "matters": ["warehouse back injury", "repetitive strain injury", "construction site fall", "delivery driver injury"],
        "fee": "a fee capped at 15 percent of benefits, as set by the state board",
        "fee_short": "the 15 percent cap",
    },
}

# One coherent injury per scenario: (body part, diagnosis, imaging test, treatment, notes document).
INJURY_PROFILES = [
    ("lower back", "herniated disc", "an MRI", "physical therapy", "Physical therapy notes"),
    ("right shoulder", "torn rotator cuff", "an MRI", "physical therapy", "Physical therapy notes"),
    ("wrist", "sprained wrist", "X-rays", "a brace and hand therapy", "Hand therapy notes"),
    ("neck", "whiplash injury", "X-rays", "chiropractic care", "Chiropractic notes"),
    ("left knee", "torn meniscus", "an MRI", "physical therapy", "Physical therapy notes"),
    ("ankle", "fractured ankle", "X-rays", "a walking boot and physical therapy", "Physical therapy notes"),
]
TEST_REPORT = {"an MRI": "MRI report", "X-rays": "X-ray report", "a CT scan": "CT scan report"}
EMPLOYMENT_MATTER_SENTENCE = {
    "wrongful termination": "They fired me two weeks after I complained, and the reason they gave doesn't add up.",
    "unpaid overtime": "I was working fifty-hour weeks and they only ever paid me for forty.",
    "workplace retaliation": "Right after I filed the complaint, they moved me to the worst shifts.",
    "disability discrimination": "I asked for a schedule accommodation for my condition, and they said no without even discussing it.",
}

SLOTS = {
    "time": ["7:30 in the morning", "around noon", "a little after 5 pm", "about 9 at night", "early afternoon", "right at rush hour"],
    "place": ["the intersection of Fifth and Grant", "the grocery store on Elm", "the warehouse loading dock", "the parking garage downtown",
              "my apartment complex", "the bus stop on Riverside", "the highway on-ramp", "the hardware store"],
    "errand": ["pick up my daughter", "my night shift", "the pharmacy", "a job interview", "my mom's place", "the gym"],
    "clinic": ["Valley Urgent Care", "St. Anne's Medical Center", "Westside Clinic", "Mercy General", "the county hospital"],
    "n_days": ["six", "ten", "twelve", "about fifteen", "almost twenty"],
    "employer": ["Brightline Logistics", "Cascade Foods", "Summit Home Health", "Delta Freight", "Northstar Retail", "Pinecrest Builders"],
    "insurer": ["Pacific Mutual", "Granite State Insurance", "Allied Shield", "Keystone Casualty", "Liberty Crest"],
    "witness": ["guy walking his dog", "woman from the store", "delivery driver", "neighbor across the street"],
    "amount": ["$1,240", "$3,875", "$612", "$9,300", "$2,150", "$480"],
    "relative": ["sister", "husband", "wife", "son", "roommate", "mom"],
    "activity": ["drive", "drive long distances"],
    "report_prefix": ["24-", "SR-", "PD-7", "IR-3"],
    "doctor": ["Dr. Okonkwo", "Dr. Reyes", "Dr. Lindgren", "Dr. Basu", "Dr. Moreau"],
    "month": ["January", "March", "April", "June", "July", "August", "September", "October"],
}

# Caller narratives. The first sentence is always the incident sentence (filled from the
# incident date on file); the rest are sampled from the banks that fit the practice and kept
# in bank order so the story reads in sequence. Slot values are fixed per scenario.
NARRATIVE_INCIDENT = {
    "injury": "So it happened on {incident_spoken}, {time}, near {place}.",
    "wc": "So it happened on {incident_spoken}, during my shift at {employer}.",
    "employment": "So it all came to a head on {incident_spoken}, at {employer}.",
}
NARRATIVE = {
    "injury": [
        "Honestly I didn't think much of it at first, but by that night my {body} was killing me.",
        "I went to {clinic} the next morning and they sent me for {test}.",
        "The doctor said it was a {injury} and put me on {treatment}.",
        "{work_sentence}",
        "Someone from {insurer} called me twice last week asking for a recorded statement. I didn't give one, because you all told me to send them to you.",
        "There was a witness, a {witness}, who gave me their number.",
        "I took a few photos with my phone but some of them are kind of blurry.",
        "The bills are starting to pile up. I got one from {clinic} for {amount}.",
        "I'm still doing {treatment} and it's helping a little.",
        "My {relative} has been driving me to appointments because I can't really {activity}.",
        "Sleep has been rough. I wake up a few times a night because of the pain.",
        "I kept all my receipts from the pharmacy and the parking at the hospital.",
    ],
    "street": ["I was on my way to {errand} when everything went sideways."],
    "auto": [
        "There was a police report. I think the number starts with {report_prefix}.",
        "The other driver's insurance keeps saying it was partly my fault, which isn't true.",
    ],
    "employment": [
        "{matter_sentence}",
        "My supervisor stopped including me in meetings right after I raised it with HR.",
        "I saved the emails and the texts from my supervisor, like you asked.",
        "A coworker named Pat saw most of it and said they'd back me up.",
        "I've been applying for other jobs, but nothing has come through yet.",
        "HR said they'd look into it, but I haven't heard anything back.",
    ],
    "common": [
        "I'm the main income for my household, so this has been stressful.",
        "I just want to make sure I'm not missing anything important.",
        "I'm worried about how long this is all going to take.",
        "I have a folder with all the paperwork, but I'm not sure what matters.",
        "My {relative} keeps asking me how the case is going.",
        "I wrote down everything I remembered that same week, in a notes app on my phone.",
        "A friend of mine went through something similar and said it took about a year.",
    ],
}

EMPATHY = [
    "I'm really sorry you're dealing with all of that, {first}. Thank you for walking me through it; those details help the attorney a lot.",
    "That sounds exhausting, {first}. You're doing the right thing by keeping your paperwork together.",
    "Thanks for explaining all of that. It's very common to feel unsure about the process, and that's exactly what we're here for.",
    "I appreciate you sharing that. It helps {attorney} see the full picture.",
    "That's a lot to carry, {first}. Let's take it one step at a time.",
    "Thank you. It sounds like you've been careful about keeping records, which really helps.",
]
# Follow-up questions with replies that answer them. Keys: which practices they fit, and
# whether they need a sentence of the story (e.g. a witness) to have been told.
FOLLOWUP = [
    {"q": "Have you been back to the doctor since then?", "for": ("injury",), "key": "doctor"},
    {"q": "Do you still have the contact details for that witness?", "for": ("injury",), "needs": "witness",
     "a": ["Yeah, I have them saved."]},
    {"q": "Did you report it to anyone at the time it happened?", "for": ("injury", "employment"),
     "a": ["Yes, I reported it that same day."]},
    {"q": "Are you able to work right now?", "for": ("injury", "employment"), "key": "work"},
    {"q": "Has anyone asked you to sign anything since we last talked?", "for": ("injury", "employment"),
     "a": ["No, nothing.", "No, and I'd check with you first anyway."]},
    {"q": "Is there anything else about that day you think we should know?", "for": ("injury", "employment"),
     "a": ["Not that I can think of.", "No, I think that's everything."]},
]

# FAQ topics: questions, KB article title, article sentences, short spoken answer.
FAQ = [
    {
        "key": "fees", "topic": "how the contingency fee works",
        "q": ["Can you remind me how your fee works?", "What's your cut again if this settles?", "Do I owe anything upfront?", "How much does the firm take at the end?", "Is your fee a percentage?"],
        "title": "Understanding our fee agreement",
        "s": [
            "Most matters are handled under {fee}.",
            "Clients pay no attorney fee unless there is a recovery.",
            "The percentage is calculated from the gross recovery before case costs are reimbursed, unless the agreement states otherwise.",
            "Clients receive a written closing statement showing every fee and cost before any funds are disbursed.",
            "Fee terms are explained in plain language before signing, and clients may ask for a copy in Spanish or Vietnamese.",
            "If the firm withdraws from a case, the agreement explains how fees for completed work are handled.",
            "Hourly matters, which are rare, are billed in six-minute increments and require a separate engagement letter.",
        ],
        "a": ["It's {fee}, and you only pay if there's a recovery. Nothing is due upfront.",
              "Our fee is {fee}, paid only from a recovery. You'd see a full written breakdown before any money is paid out."],
    },
    {
        "key": "costs", "topic": "case costs versus attorney fees",
        "q": ["Are there other costs besides the percentage?", "What about court fees and stuff like that?", "Will I get billed for things like records and filing fees?", "Who pays for expenses along the way?"],
        "title": "Case costs and expenses",
        "s": [
            "Case costs are separate from attorney fees and include filing fees, deposition transcripts, medical record charges, and expert fees.",
            "The firm advances case costs during the matter.",
            "Advanced costs are reimbursed from the recovery and are itemized on the closing statement.",
            "If there is no recovery, clients are not asked to repay advanced costs, except where the agreement says otherwise for voluntary dismissals.",
            "Large expenses, such as expert retention above $2,500, are discussed with the client before they are incurred.",
            "Clients can request a running cost ledger at any time through their paralegal.",
        ],
        "a": ["Costs like filing fees and records are separate, but the firm advances them and they come out of any recovery. You'd see them itemized.",
              "There are case costs, like records and filing fees. We front those, and they're listed line by line at the end."],
    },
    {
        "key": "timeline", "topic": "how long a case usually takes",
        "q": ["How long does something like this usually take?", "Am I looking at months or years here?", "When do you think this will wrap up?", "Is there any way to know how long this will take?"],
        "title": "Typical case timelines",
        "s": [
            "Many claims resolve within nine to eighteen months, but every case is different.",
            "Cases usually cannot be valued until the client has finished treatment or reached maximum medical improvement.",
            "Once treatment ends, the firm gathers records and bills, which commonly takes six to ten weeks.",
            "A demand package is then sent to the insurer, and insurers often take thirty to sixty days to respond.",
            "If a fair offer is not made, the attorney may recommend filing a lawsuit, which can add a year or more.",
            "Only the attorney can give a case-specific estimate of how long a matter will take.",
        ],
        "a": ["It really depends on the case. A lot of them take somewhere around nine to eighteen months, and your attorney can give you a better sense once treatment wraps up.",
              "It varies a lot, so I can't promise a timeline. Usually things can't be valued until you're done with treatment."],
    },
    {
        "key": "documents", "topic": "which documents to gather",
        "q": ["What paperwork should I be pulling together?", "What documents do you need from me?", "Is there anything else I should be gathering?", "Which papers matter most for a case like mine?"],
        "title": "Documents to gather",
        "s": [
            "Helpful documents include medical bills, visit summaries, photos, the police or incident report, and insurance cards.",
            "For lost wages, recent pay stubs and a letter from the employer confirming missed time are useful.",
            "Clients should keep a simple log of symptoms, appointments, and out-of-pocket expenses.",
            "Original documents should be kept by the client; copies or phone photos are fine for the firm.",
            "Documents can be uploaded through the client portal or emailed to the assigned paralegal.",
            "Clients should not alter or annotate original records before sending them.",
        ],
        "a": ["The big ones are medical bills, any photos, the incident report, and your insurance info. Pay stubs too if you've missed work.",
              "Medical bills and visit summaries, photos, the report number, and pay stubs if you've lost time at work. Phone photos are totally fine."],
    },
    {
        "key": "medical", "topic": "who pays medical bills while the case is open",
        "q": ["Who's supposed to pay my medical bills right now?", "Should I be using my own health insurance?", "The hospital keeps sending me bills. What do I do with them?", "Should I keep paying my medical bills myself?"],
        "title": "Medical bills during an open claim",
        "s": [
            "Clients should generally continue using their own health insurance for treatment while a claim is pending.",
            "Some providers will treat on a lien, meaning they are paid from the eventual recovery.",
            "The firm can send letters of protection to providers when appropriate.",
            "Clients should forward any collections notices to their paralegal promptly.",
            "Health insurers may have a right to reimbursement from the recovery, and the firm negotiates those amounts.",
            "Clients should talk to their doctor, not the firm, about any change in treatment.",
        ],
        "a": ["Generally you'd keep using your own health insurance for now, and if you get any collections notices, send them to your paralegal.",
              "Usually your own insurance first. Some providers will wait to be paid from the case, and we can help with letters for that."],
    },
    {
        "key": "adjuster", "topic": "talking to the insurance adjuster",
        "q": ["The insurance company keeps calling me. Should I talk to them?", "Do I have to give the adjuster a statement?", "An adjuster left me a voicemail. Do I call back?", "What do I say if the insurance company calls again?"],
        "title": "Contact from insurance adjusters",
        "s": [
            "Once represented, clients may refer all insurer calls to the firm.",
            "Clients should not give recorded statements to the other party's insurer without speaking to their attorney.",
            "Clients should not sign medical authorizations or releases sent by an insurer without review.",
            "The firm sends a letter of representation so adjusters contact the firm directly.",
            "Clients must still cooperate with their own insurer as their policy requires, ideally with the firm's guidance.",
        ],
        "a": ["You can just tell them you're represented and give them our number. Please don't give a recorded statement or sign anything until your attorney looks at it.",
              "Best to hold off. Since we're representing you, we've told them to call us instead."],
    },
    {
        "key": "social", "topic": "social media during a case",
        "q": ["Is it okay if I keep posting on Instagram?", "Should I stay off social media?", "Can I post pictures from my weekend?", "Do I need to make my accounts private?"],
        "title": "Social media guidance",
        "s": [
            "Insurers and defense counsel routinely review claimants' public social media.",
            "Clients should avoid posting about the incident, injuries, activities, or the case.",
            "Clients should not delete existing posts, since deleting content can create legal problems.",
            "Privacy settings help but do not guarantee content stays private.",
            "Clients should ask friends and family not to tag them in photos or posts during the case.",
        ],
        "a": ["It's best not to post about the accident, your injuries, or your activities. And please don't delete anything that's already up.",
              "I'd keep it quiet for now. Insurers do look, so avoid posting about the case or what you're up to, but don't delete old posts."],
    },
    {
        "key": "wages", "topic": "proving lost wages",
        "q": ["Can I get paid back for the work I missed?", "How do I prove I lost income?", "Does the case cover the paychecks I missed?", "What do I need to show for the time I was out?"],
        "title": "Lost wages and income",
        "s": [
            "Lost wages may be part of a claim when an injury caused missed work.",
            "Proof usually includes pay stubs, tax returns, and a wage-loss letter from the employer.",
            "Self-employed clients can use invoices, bank statements, and prior-year returns.",
            "A doctor's note supporting time off strengthens the claim.",
            "The paralegal can send the employer a standard wage verification form.",
        ],
        "a": ["Missed work can be part of the claim. Pay stubs and a letter from your employer are the main proof, and your paralegal has a form for that.",
              "Missed work can be part of the claim. We'd want pay stubs and a note from your doctor about the time off."],
    },
    {
        "key": "sol", "topic": "filing deadlines",
        "q": ["Is there a deadline for this?", "Am I running out of time to file?", "How long do I have to bring this claim?", "When is the cutoff for filing?"],
        "title": "Statutes of limitations",
        "s": [
            "Every claim has a legal deadline, called a statute of limitations, which varies by claim type and state.",
            "Claims against government entities often require a written notice within six months.",
            "Missing a deadline can bar a claim entirely.",
            "An estimated date can come from the firm's deadline calculator, but only an attorney can confirm it.",
            "Deadlines are calendared by the paralegal team at intake and reviewed by the assigned attorney.",
        ],
        "a": ["There is a deadline, and it depends on the type of claim. Your attorney will confirm it, but it's one reason not to wait.",
              "There are deadlines, and they vary. If a government agency is involved it can be as short as six months, so the attorney will confirm yours."],
    },
    {
        "key": "consult", "topic": "what happens at a case review meeting",
        "q": ["What happens at a case review meeting?", "What should I bring to a meeting with the attorney?", "How long does a meeting with the attorney take?", "Can I do the attorney meeting by video?"],
        "title": "Preparing for a meeting with your attorney",
        "s": [
            "Case review meetings last about forty-five minutes, and there is no charge for them.",
            "Clients should bring photo identification, insurance cards, and any documents or photos about the incident.",
            "The attorney will review the facts, explain options, and answer questions about the process.",
            "Clients may bring a family member, though the attorney may ask to speak privately for part of the meeting.",
            "Video consultations are available for clients who cannot travel.",
        ],
        "a": ["There's no charge, and it's about forty-five minutes. Bring your ID, insurance cards, and anything you have about what happened.",
              "The attorney goes over what happened and your options. Bring ID and whatever paperwork or photos you have; video works too."],
    },
    {
        "key": "confidential", "topic": "confidentiality",
        "q": ["Is what I tell you confidential?", "Will my employer find out I called?", "Who can see what I tell you?", "Does anyone else find out about my case?"],
        "title": "Confidentiality and privacy",
        "s": [
            "Communications made to seek legal advice are generally confidential.",
            "The firm does not contact employers or other parties without the client's permission.",
            "Call recordings and notes are stored in the firm's secure case management system.",
            "Clients can ask which staff members have access to their file.",
            "Case details are shared only with the verified client or the client's authorized contacts.",
        ],
        "a": ["What you share with us is kept confidential, and we won't contact your employer without your permission.",
              "It's confidential. We don't reach out to anyone on your behalf unless you say it's okay."],
    },
    {
        "key": "settlement", "topic": "how settlements work",
        "q": ["How does a settlement actually work?", "Do I get a say in whether we settle?", "Who decides if we take an offer?", "How do I get paid if we settle?"],
        "title": "How settlements work",
        "s": [
            "The client always decides whether to accept or reject a settlement offer.",
            "The attorney will explain the offer, likely outcomes, and the net amount after fees and costs.",
            "Settlement funds are deposited into the firm's trust account before disbursement.",
            "Liens and medical balances are resolved before the client's share is released.",
            "Clients receive a closing statement to review and sign before funds are released.",
        ],
        "a": ["You always make the final call on any offer. The attorney walks you through it and what you'd actually take home.",
              "It's your decision. Money goes into the firm's trust account, bills and liens get paid, and you sign off on a statement before your share is released."],
    },
    {
        "key": "office", "topic": "office location, hours, and parking",
        "q": ["Where exactly is your office, and is there parking?", "What are your hours, and where do I park?", "What time do you close, and where is the office?", "Is there parking near your office, and when are you open?"],
        "title": "Office location and parking",
        "s": [
            "The main office is at {address}, on the third floor.",
            "Office hours are Monday through Friday, 8:30 am to 5:30 pm, with evening appointments on Thursdays.",
            "Validated parking is available in the garage behind the building; bring the ticket to reception.",
            "The office is two blocks from the downtown transit center.",
            "The building is wheelchair accessible, with an elevator at the north entrance.",
        ],
        "a": ["We're at {address}, third floor, open 8:30 to 5:30 on weekdays. There's validated parking in the garage behind the building; just bring your ticket to the front desk.",
              "The office is at {address}, and we're open 8:30 to 5:30 on weekdays. Parking in the garage behind us is validated."],
    },
    {
        "key": "updates", "topic": "how often the firm gives updates",
        "q": ["How often will I hear from you guys?", "Who do I call if I have questions later?", "How will I know when something happens on my case?", "When should I expect my next update?"],
        "title": "Case updates and communication",
        "s": [
            "Clients receive a status update at least every thirty days, or sooner when something important happens.",
            "Each client has an assigned paralegal as their main point of contact.",
            "Messages left during business hours are returned within one business day.",
            "Clients can check case milestones in the client portal.",
            "Urgent matters, such as a new lawsuit or a settlement deadline, are escalated to the attorney the same day.",
        ],
        "a": ["You'll get an update at least every thirty days, and your paralegal is your main contact. Calls get returned within a business day.",
              "Your paralegal is your go-to person, and you'll hear from us at least monthly."],
    },
    {
        "key": "interpreter", "topic": "interpreter services",
        "q": ["My mom speaks mostly Spanish. Can she be on the calls?", "Do you have interpreters?", "Can someone translate for my dad?", "Is there anyone there who speaks Spanish?"],
        "title": "Language access",
        "s": [
            "Interpreter services are available at no charge for consultations and client meetings.",
            "Staff members speak Spanish, Vietnamese, and Tagalog.",
            "Clients may designate a family member as an authorized contact by signing a short form.",
            "Important documents can be translated into the client's preferred language.",
        ],
        "a": ["Interpreters are free, and we have Spanish speakers on staff. A family member can be an authorized contact once you sign a short form.",
              "Interpreters are available at no charge, and we can also translate the key documents."],
    },
    {
        "key": "property", "topic": "property damage and car repairs",
        "q": ["What about my car? It's still sitting at the body shop.", "Who pays for the damage to my car?", "Do you handle the car damage too?", "Is my car repair part of this case?"],
        "title": "Property damage claims",
        "s": [
            "Property damage is usually handled separately from the injury claim and often resolves sooner.",
            "Clients may use their own collision coverage and seek reimbursement of the deductible.",
            "Rental car coverage depends on the policies involved.",
            "Clients should photograph damage and keep repair estimates and invoices.",
            "Storage fees at body shops can accumulate quickly, so delays should be avoided.",
        ],
        "a": ["Car damage is usually handled separately and faster. Keep the estimates, and watch out for storage fees at the shop.",
              "That's typically a separate claim. You can use your own collision coverage and we try to get your deductible back."],
    },
]

# Employment versions of FAQ entries whose injury wording does not fit an employment matter.
FAQ_EMPLOYMENT = {
    "documents": {
        "s": [
            "Helpful documents include the offer letter, pay stubs, timesheets, performance reviews, and any termination or discipline letters.",
            "Emails and texts with supervisors or HR are often the most important evidence, so clients should save them.",
            "Clients should keep a simple log of dates, conversations, and who was present.",
            "Original documents should be kept by the client; copies or phone screenshots are fine for the firm.",
            "Documents can be uploaded through the client portal or emailed to the assigned paralegal.",
            "Clients should not take company documents they are not allowed to access.",
        ],
        "a": ["The big ones are your pay stubs, timesheets, any letters from HR, and the emails or texts with your supervisor.",
              "Pay records, performance reviews, anything in writing from HR, and screenshots of messages. Phone screenshots are fine."],
    },
    "timeline": {
        "s": [
            "Many employment claims resolve within nine to eighteen months, but every case is different.",
            "Some claims must first go through a government agency, which can take several months to respond.",
            "The firm gathers pay records, personnel files, and witness accounts before making a demand.",
            "If a fair offer is not made, the attorney may recommend filing a lawsuit, which can add a year or more.",
            "Only the attorney can give a case-specific estimate of how long a matter will take.",
        ],
        "a": ["It really depends on the case. A lot of them take somewhere around nine to eighteen months, and some steps go through an agency first.",
              "It varies a lot, so I can't promise a timeline. Agency steps alone can take a few months."],
    },
    "wages": {
        "s": [
            "Lost pay may be part of an employment claim, including back pay and unpaid overtime.",
            "Proof usually includes pay stubs, timesheets, tax returns, and records of hours worked.",
            "Clients who find new work should keep their new pay records too.",
            "The paralegal can request payroll records from the employer.",
        ],
        "a": ["Lost pay can be part of the claim. Pay stubs and timesheets are the main proof, and your paralegal can request payroll records.",
              "Missed pay can be part of the claim. Keep your pay stubs and any record of the hours you worked."],
    },
    "consult": {
        "s": [
            "Case review meetings last about forty-five minutes, and there is no charge for them.",
            "Clients should bring photo identification and any documents, emails, or messages about the dispute.",
            "The attorney will review the facts, explain options, and answer questions about the process.",
            "Video meetings are available for clients who cannot travel.",
        ],
        "a": ["There's no charge, and it's about forty-five minutes. Bring your ID and anything in writing about what happened.",
              "The attorney goes over where things stand and your options. Bring ID and any emails or messages you have; video works too."],
    },
    "social": {
        "s": [
            "Employers and their lawyers routinely review employees' public social media.",
            "Clients should avoid posting about the employer, coworkers, or the case.",
            "Clients should not delete existing posts, since deleting content can create legal problems.",
            "Privacy settings help but do not guarantee content stays private.",
        ],
        "a": ["It's best not to post about your job, your old coworkers, or the case. And please don't delete anything that's already up.",
              "I'd keep it quiet for now. Employers do look, so avoid posting about work or the case, but don't delete old posts."],
    },
}

GREETINGS = [
    "Hi, this is {first} {last}. I'm calling about my case.",
    "Hey, um, I spoke with someone last week, and I'm calling back. It's {first} {last}.",
    "Hello? Yes, hi, this is {first}. {first} {last}. I had some questions.",
    "Hi there, my name is {first} {last}. I think I have a file with you.",
]

DOC_NAMES = {
    "common": ["Photo ID", "Pay stubs (last 3 months)"],
    "injury": ["Health insurance card", "Employer wage-loss letter", "Pharmacy receipts", "Incident photos"],  # plus test report, notes, visit summary
    "auto": ["Auto insurance declarations page", "Police report", "Repair estimate"],
    "employment": ["Performance reviews", "Text messages with supervisor", "Offer letter", "Timesheets"],
}
CASE_STAGES = ["intake review", "investigation", "treatment monitoring", "records collection", "demand preparation", "negotiation", "litigation: discovery"]
ACTIVITY_TYPES = ["records request sent", "call with client", "insurer letter received", "medical bill logged", "status letter mailed", "attorney review"]
ACTIVITY_NOTES = [
    "Requested updated records from the treating clinic.",
    "Insurer acknowledged the letter of representation.",
    "Client reported continued pain and ongoing therapy.",
    "Received an itemized bill and logged it to the damages sheet.",
    "Attorney reviewed liability photos; no action needed.",
    "Left a voicemail for the adjuster about the claim number.",
]
NEXT_STEPS = [
    "collect the remaining medical records", "confirm the end of treatment", "prepare the demand package",
    "follow up with the adjuster", "schedule a client check-in call", "request the employer wage letter",
]

POLICY_TITLES = [
    "Intake and conflict checks", "Identity verification", "Communication standards", "Handling distressed callers",
    "Records and privacy", "Escalation to attorneys", "After-hours calls", "Referrals and declined matters",
    "Payments and refunds", "Scheduling rules", "Document handling", "Accessibility", "Complaints",
    "Media and third parties", "Retention of call notes", "Holiday coverage",
]
POLICY_SENTENCES = [
    "Staff and assistants must run a conflict check before discussing the merits of a new matter.",
    "If a caller names an opposing party already in our system, pause and route the call to intake staff.",
    "Verify identity with two of the following: date of birth, address on file, last four digits of phone, or client ID.",
    "Do not read back full Social Security numbers, account numbers, or medical record numbers.",
    "Use the caller's preferred name and keep a calm, unhurried tone.",
    "If a caller mentions self-harm, provide the crisis line and transfer to the on-call staff member immediately.",
    "Never speculate about the value of a case or the likelihood of success.",
    "Summaries of calls are saved to the file within fifteen minutes of the call ending.",
    "Callers asking for legal advice should be offered a consultation rather than an answer.",
    "Escalate same-day any mention of a lawsuit being served, a court date, or a settlement deadline.",
    "After-hours callers can leave a message or book a callback for the next business day.",
    "Declined matters receive a written non-engagement letter within three business days.",
    "Refunds may be issued only for duplicate or erroneous charges, up to $500, without manager approval.",
    "Appointments may be booked only into slots returned by the availability tool.",
    "Documents sent for signature must use the current approved template for the matter type.",
    "Offer large-print and translated documents on request.",
    "Complaints are logged and routed to the office manager within one business day.",
    "Do not confirm or deny representation to reporters or unknown third parties.",
    "Call notes are retained for seven years after a matter closes.",
    "During holidays, the on-call attorney rotation is posted in the staff calendar.",
    "If a tool is unavailable, tell the caller and create a follow-up task rather than guessing.",
    "Authorized contacts may receive scheduling information but not case strategy.",
    "Texts may include office addresses and appointment times but never medical details.",
    "Emails to clients must come from the firm's verified domain and include the matter number.",
    "Interpreters must be offered at the start of the call when the caller prefers another language.",
    "When in doubt about a caller's identity, end the discussion politely and offer a callback to the number on file.",
    "Never instruct a caller to stop medical treatment or change providers.",
    "If a caller is driving, offer to call back later.",
    "Keep hold times under two minutes and check back with the caller if a lookup is slow.",
]
STAFF_ROLES = ["Paralegal", "Intake specialist", "Case manager", "Billing coordinator", "Receptionist", "Attorney", "Records clerk"]
