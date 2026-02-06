import json
import random

def generate_intents():
    intents = []

    # 1. General Conversation (10 intents)
    general_tags = [
        ("greeting", ["Hi", "Hello", "Hey", "Good morning"], ["Hello! How can I help you regarding your health?", "Hi there! What brings you here?"]),
        ("goodbye", ["Bye", "See you", "Goodbye"], ["Stay healthy! Goodbye.", "Take care!"]),
        ("thanks", ["Thanks", "Thank you"], ["You're welcome!", "Glad I could help."]),
        ("options", ["What can you do?", "Help"], ["I can analyze symptoms, answer health questions, and help with appointments."]),
        ("identity", ["Who are you?", "Are you human?"], ["I am an AI healthcare assistant."]),
        ("jokes", ["Tell me a joke"], ["Why did the banana go to the doctor? It wasn't peeling well!"]),
        ("mood_happy", ["I am happy", "Feeling good"], ["That's great! Mental well-being is important."]),
        ("mood_sad", ["I am sad", "Feeling low"], ["I'm sorry to hear that. Talking to a friend or professional might help."]),
        ("weather", ["What's the weather?"], ["I am a healthcare bot, unlikely to know the weather, but I can check if you have a cold!"]),
        ("name", ["What is your name?"], ["I am your HealthBot assistant."])
    ]
    for tag, patterns, responses in general_tags:
        intents.append({"tag": tag, "patterns": patterns, "responses": responses})

    # 2. Administrative / Hospital (20 intents)
    departments = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Dermatology", "Gynecology", "Oncology", "Psychiatry", "Urology", "ENT", "Ophthalmology", "Dental", "General Surgery", "Internal Medicine", "Radiology", "Pathology", "Emergency", "Pharmacy", "Physiotherapy", "Nutrition"]
    
    for dept in departments:
        tag = f"dept_{dept.lower().replace(' ', '_')}"
        patterns = [f"{dept} department", f"Book {dept}", f"Is {dept} open?", f"I need a {dept} doctor"]
        responses = [f"The {dept} department is on the 2nd floor. Open 9 AM - 5 PM.", f"You can book an appointment for {dept} via our reception."]
        intents.append({"tag": tag, "patterns": patterns, "responses": responses})

    # 3. Medical Conditions & Symptoms (150+ intents)
    # List of (Condition, Symptoms list, Simple Advice)
    conditions = [
        ("Flu", ["start of flu", "flu symptoms", "body ache and fever"], "Rest, fluids, and antipyretics."),
        ("Common Cold", ["runny nose", "sneezing", "cold symptoms"], "Stay hydrated, rest, and take vitamin C."),
        ("COVID-19", ["loss of taste", "covid symptoms", "high fever and dry cough"], "Isolate yourself and get tested."),
        ("Migraine", ["one sided headache", "migraine aura", "severe headache"], "Rest in a dark room. Take prescribed meds if any."),
        ("Hypertension", ["high blood pressure", "dizziness and bp", "hypertension symptoms"], "Reduce salt, manage stress, and see a doctor."),
        ("Diabetes", ["high blood sugar", "excessive thirst", "frequent urination"], "Monitor blood sugar, avoid sweets, and consult an endocrinologist."),
        ("Asthma", ["wheezing", "shortness of breath", "asthma attack"], "Use your inhaler and sit upright. Seek help if it worsens."),
        ("Gastritis", ["burning stomach", "acidity", "gastric pain"], "Avoid spicy food, eat small meals, and stay hydrated."),
        ("Anemia", ["fatigue", "pale skin", "weakness"], "Eat iron-rich foods like spinach and meat. Consult a doctor."),
        ("Insomnia", ["can't sleep", "trouble sleeping", "insomnia"], "Maintain a sleep schedule, avoid caffeine, and reduce screen time."),
        ("Arthritis", ["joint pain", "stiff joints", "arthritis"], "Gentle exercise and anti-inflammatory medication can help."),
        ("Allergy", ["itchy skin", "allergic reaction", "hives"], "Identify the trigger and take an antihistamine."),
        ("Depression", ["feeling hopeless", "loss of interest", "depressed"], "Please reach out to a mental health professional or a trusted friend."),
        ("Anxiety", ["panic attack", "anxious", "nervousness"], "Try deep breathing exercises. Ground yourself in the present."),
        ("Acne", ["pimples", "acne breakout", "skin spots"], "Keep your face clean, avoid touching it, and use non-comedogenic products."),
        ("Eczema", ["itchy dry skin", "eczema flare", "skin rash"], "Moisturize frequently and avoid harsh soaps."),
        ("Conjunctivitis", ["pink eye", "itchy eyes", "eye discharge"], "Wash hands, avoid touching eyes, and see an ophthalmologist."),
        ("Ear Infection", ["ear pain", "ear blockage", "ear ache"], "Keep ear dry. Consult a doctor for antibiotics if needed."),
        ("Sinusitis", ["blocked nose", "sinus pain", "facial pressure"], "Steam inhalation and saline sprays can provide relief."),
        ("Sore Throat", ["throat pain", "pain swallowing", "scratchy throat"], "Warm salt water gargle and honey can soothe it."),
        ("Dehydration", ["thirsty", "dark urine", "dry mouth"], "Drink clear fluids and oral rehydration salts."),
        ("Heat Stroke", ["high body temp", "no sweating", "heat exhaustion"], "Move to a cool place and cool the body down immediately."),
        ("Burn", ["skin burn", "scald", "blisters"], "Run cool water over the burn for 20 minutes. Do not pop blisters."),
        ("Cut", ["bleeding cut", "open wound", "laceration"], "Apply pressure to stop bleeding and clean with water."),
        ("Sprain", ["twisted ankle", "swollen joint", "sprain"], "R.I.C.E: Rest, Ice, Compression, Elevation."),
        ("Fracture", ["broken bone", "severe bone pain", "deformity"], "Immobilize the area and go to the ER immediately."),
        ("Food Poisoning", ["vomiting", "bad stomach", "ate bad food"], "Stay hydrated. Avoid solid food until vomiting stops."),
        ("Sunburn", ["red skin", "sun burn", "burning skin"], "Apply aloe vera and stay out of the sun."),
        ("Dandruff", ["flaky scalp", "white flakes", "dandruff"], "Use an anti-dandruff shampoo containing zinc pyrithione."),
        ("Hair Loss", ["losing hair", "hair thinning", "baldness"], "Consult a dermatologist to find the cause."),
        ("Obesity", ["overweight", "weight gain", "obesity risk"], "Balanced diet and regular exercise are key. Consult a dietician."),
        ("Malaria", ["shivering fever", "mosquito bite fever", "malaria symptoms"], "Immediate blood test and medical treatment required."),
        ("Typhoid", ["prolonged fever", "typhoid symptoms", "stomach pain fever"], "Antibiotics and hygiene are crucial. See a doctor."),
        ("Dengue", ["platelet drop", "bone breaking pain", "dengue fever"], "Fluid management is critical. Monitor platelets."),
        ("Chickenpox", ["itchy blisters", "pox marks", "chickenpox"], "Rest, calamine lotion, and isolation."),
        ("Pneumonia", ["chest congestion", "productive cough", "lung infection"], "Requires medical assessment and possibly antibiotics."),
        ("Bronchitis", ["cough", "chest cold", "bronchitis"], "Rest and fluids. See a doctor if breathing is difficult."),
        ("Tuberculosis", ["coughing blood", "night sweats", "weight loss tb"], "Strict adherence to antibiotic course required. See a specialist."),
        ("Kidney Stones", ["sharp back pain", "blood in urine", "renal colic"], "Drink lots of water. Pain management and medical advice needed."),
        ("UTI", ["burning urine", "frequent urination pain", "urinary infection"], "Drink water and cranberry juice. Antibiotics may be needed."),
        ("Psoriasis", ["silvery scales", "psoriasis patches", "skin plaques"], "Topical treatments and phototherapy can help."),
        ("Rosacea", ["red face", "facial flushing", "rosacea"], "Identify triggers like spicy food or sun/heat."),
        ("Scabies", ["intense itching", "night itch", "scabies mites"], "Prescription cream is needed for the whole range."),
        ("Vertigo", ["spinning sensation", "dizzy spells", "vertigo"], "Lie down. Vestibular exercises may help."),
        ("Tinnitus", ["ringing in ears", "ear noise", "tinnitus"], "Avoid loud noises. Consult an ENT if persistent."),
        ("Gingivitis", ["bleeding gums", "swollen gums", "gum disease"], "Brush and floss daily. See a dentist."),
        ("Toothache", ["tooth pain", "cavity pain", "sensitive tooth"], "Rinse with warm salt water. See a dentist."),
        ("Bad Breath", ["halitosis", "smelly breath", "bad breath"], "Oral hygiene and hydration. Check for dental issues."),
        ("Dry Eye", ["gritty eyes", "dry eyes", "eye irritation"], "Use artificial tears. Blink more often."),
        ("Cataract", ["cloudy vision", "blurred vision", "cataract"], "Surgery is the only effective treatment."),
        ("Glaucoma", ["eye pressure", "tunnel vision", "glaucoma"], "Regular eye drops and checkups are essential."),
        ("Hypothyroidism", ["weight gain", "cold intolerance", "slow metabolism"], "Thyroid hormone replacement therapy is usually needed."),
        ("Hyperthyroidism", ["weight loss", "fast heart rate", "overactive thyroid"], "Medication or radioactive iodine treatment."),
        ("Osteoporosis", ["brittle bones", "frequent fractures", "low bone density"], "Calcium, Vitamin D, and weight-bearing exercises."),
        ("Gout", ["toe pain", "high uric acid", "joint redness"], "Diet changes (low purine) and medication."),
        ("Carpal Tunnel", ["wrist pain", "numb fingers", "mouse hand"], "Wrist splints, breaks, and ergonomic setup."),
        ("Back Pain", ["lower back pain", "lumbago", "back ache"], "Posture correction, stretching, and core strengthening."),
        ("Neck Pain", ["stiff neck", "neck ache", "cervical pain"], "Ergonomic pillow and neck exercises."),
        ("Scoliosis", ["curved spine", "uneven shoulders", "scoliosis"], "Monitoring, bracing, or surgery depending on severity."),
        ("Varicose Veins", ["swollen veins", "leg veins", "varicose"], "Compression stockings and leg elevation."),
        ("Deep Vein Thrombosis", ["leg swelling", "calf pain", "DVT"], "Medical emergency. Risks pulmonary embolism."),
        ("Heart Attack", ["chest pressure", "arm pain", "myocardial infarction"], "CALL EMERGENCY IMMEDIATELY. Chew aspirin if advised."),
        ("Stroke", ["face drooping", "arm weakness", "slurred speech"], "CALL EMERGENCY. Time is brain."),
        ("Arrhythmia", ["palpitations", "irregular heartbeat", "skipped beats"], "Cardiologist evaluation needed."),
        ("Heart Failure", ["swollen ankles", "breathlessness", "heart failure"], "Strict medication and diet adherence."),
        ("Cholesterol", ["high lipid", "ldl cholesterol", "high cholesterol"], "Diet, exercise, and statins if prescribed."),
        ("Appendicitis", ["right lower stomach pain", "rebound tenderness", "appendix"], "Emergency surgery usually required."),
        ("Hernia", ["groin lump", "bulge in abdomen", "hernia"], "Surgery is often needed to repair the wall."),
        ("Hemorrhoids", ["piles", "rectal pain", "blood in stool"], "High fiber diet, sitz baths."),
        ("IBS", ["irritable bowel", "bloating", "ibs symptoms"], "Dietary changes (FODMAP) and stress management."),
        ("Lactose Intolerance", ["milk gives gas", "dairy allergy", "lactose"], "Avoid dairy or use lactase enzymes."),
        ("Celiac Disease", ["gluten sensitivity", "wheat allergy", "celiac"], "Strict gluten-free diet."),
        ("Liver Disease", ["jaundice", "yellow eyes", "liver pain"], "Avoid alcohol, manage diet."),
        ("Gallstones", ["gallbladder pain", "stone pain", "gallstones"], "Surgery might be needed if symptomatic."),
        ("Pancreatitis", ["severe upper abdo pain", "pancreas inflammation", "pancreatitis"], "Hospital admission, fasting, and fluids."),
        ("Kidney Infection", ["fever and flank pain", "pyelonephritis", "kidney pain"], "Antibiotics required."),
        ("Incontinence", ["leak urine", "bladder control", "incontinence"], "Pelvic floor exercises and medical advice."),
        ("Prostate Issues", ["frequent night pee", "prostate", "bph"], "Consult a urologist."),
        ("Erectile Dysfunction", ["impotence", "ed issues", "erectile"], "Consult a doctor. Treat underlying causes."),
        ("Menopause", ["hot flashes", "periods stopping", "menopause"], "Lifestyle changes and hormone therapy if severe."),
        ("PCOS", ["irregular periods", "ovarian cysts", "pcos"], "Diet, exercise, and hormonal management."),
        ("Endometriosis", ["painful periods", "pelvic pain", "endometriosis"], "Pain management and hormonal treatments."),
        ("Pregnancy", ["morning sickness", "pregnant symptoms", "baby bump"], "Prenatal care is essential. Take folic acid."),
        ("Morning Sickness", ["nausea pregnancy", "vomiting morning", "morning sickness"], "Small frequent meals, ginger."),
        ("Labor", ["contractions", "water broke", "giving birth"], "Go to the hospital immediately."),
        ("Breastfeeding", ["latching", "nursing", "breastfeeding"], "Consult a lactation consultant."),
        ("Mastitis", ["breast pain fever", "blocked milk duct", "mastitis"], "Keep nursing/pumping. Antibiotics if fever persists."),
        ("Postpartum Depression", ["baby blues", "crying after birth", "PPD"], "Seek help. You are not alone."),
        ("Diaper Rash", ["baby bum red", "nappy rash", "rash on baby"], "Frequent changes, barrier cream, air time."),
        ("Colic", ["baby crying", "colicky baby", "fussy baby"], "Comfort measures, ensure burping."),
        ("Teething", ["baby drooling", "tooth erupting", "teething pain"], "Teething rings, cool cloth."),
        ("Croup", ["barking cough", "child noisy breathing", "croup"], "Steam or cool night air. Monitor breathing."),
        ("Measles", ["koplik spots", "measles rash", "measles"], "Vaccination is key prevention. Supportive care."),
        ("Mumps", ["swollen jaw", "mumps parotitis", "mumps"], "Isolation and pain management."),
        ("Rubella", ["german measles", "mild rash", "rubella"], "Vaccination (MMR). Danger to pregnancy."),
        ("Whooping Cough", ["pertussis", "cough vomit", "whoop sound"], "Antibiotics and vaccination."),
        ("ADHD", ["hyperactive", "can't focus", "adhd symptoms"], "Behavioral therapy and medication."),
        ("Autism", ["social difficulty", "repetitive behavior", "autism"], "Early intervention therapies."),
        ("Dyslexia", ["reading trouble", "learning disability", "dyslexia"], "Specialized education support."),
        ("Eating Disorder", ["anorexia", "bulimia", "food issue"], "Psychological and nutritional support."),
        ("Schizophrenia", ["hallucinations", "hearing voices", "schizophrenia"], "Antipsychotic medication and therapy."),
        ("Bipolar Disorder", ["mood swings", "manic depression", "bipolar"], "Mood stabilizers and therapy."),
        ("OCD", ["obsessive thoughts", "compulsive finish", "ocd"], "CBT and medication."),
        ("PTSD", ["trauma flashback", "nightmares", "ptsd"], "Trauma-focused therapy."),
        ("Alzheimer's", ["memory loss", "confusion", "dementia"], "Supportive care and safety measures."),
        ("Parkinson's", ["tremors", "shaking hand", "parkinson"], "Medication to manage symptoms."),
        ("Multiple Sclerosis", ["numbness", "vision loss ms", "multiple sclerosis"], "Immunomodulatory therapy."),
        ("ALS", ["muscle weakness", "als", "lou gehrig"], "Supportive care."),
        ("Epilepsy", ["seizures", "fits", "epilepsy"], "Anti-epileptic medication."),
        ("Bell's Palsy", ["face paralysis", "droopy face", "bell palsy"], "Steroids and eye protection."),
        ("Meningitis", ["stiff neck fever", "meningitis rash", "brain infection"], "Medical emergency. Hospital immediately."),
        ("Encephalitis", ["brain swelling", "encephalitis", "confusion fever"], "Critical care required."),
        ("Rabies", ["dog bite", "hydrophobia", "rabies risk"], "Immediate vaccination series post-bite."),
        ("Tetanus", ["lockjaw", "muscle spasms", "rusty nail"], "Tetanus shot/booster."),
        ("Lyme Disease", ["tick bite", "bullseye rash", "lyme"], "Antibiotics."),
        ("HIV", ["hiv test", "aids symptoms", "immunodeficiency"], "Antiretroviral therapy (ART)."),
        ("Gonorrhea", ["std drip", "gonorrhea", "clap"], "Antibiotics."),
        ("Syphilis", ["chancre", "syphilis rash", "std sore"], "Penicillin."),
        ("Chlamydia", ["silent std", "chlamydia", "std pain"], "Antibiotics."),
        ("Herpes", ["cold sore", "genital blister", "herpes"], "Antiviral medication."),
        ("HPV", ["warts", "hpv virus", "pap smear"], "Vaccination and monitoring."),
        ("Scorpion Sting", ["scorpion bite", "sting pain", "venom"], "Ice, pain relief. Medical help if systemic."),
        ("Snake Bite", ["venomous bite", "snake bite", "fang marks"], "Immobilize limb. Hospital IMMEDIATELY."),
        ("Bee Sting", ["bee sting allergy", "wasp sting", "sting swollen"], "Remove stinger. Ice. Epipen if allergic."),
        ("Spider Bite", ["spider venom", "recluse bite", "spider redness"], "Clean wound. Watch for necrosis."),
        ("Jellyfish Sting", ["jellyfish burn", "ocean sting", "tentacle sting"], "Vinegar rinse (for some). Hot water immersion."),
        ("Altitude Sickness", ["mountain sickness", "oxygen lack", "altitude headache"], "Descend immediately. Oxygen."),
        ("Hypothermia", ["freezing cold", "shivering stop", "hypothermia"], "Warm slowly. Dry clothes."),
        ("Frostbite", ["frozen fingers", "black toes", "frostbite"], "Warm water rewarming. Do not rub."),
        ("Choking", ["can't speak", "choking sign", "food stuck"], "Heimlich maneuver."),
        ("CPR", ["no pulse", "cardiac arrest", "cpr needed"], "Start chest compressions. Call 911."),
        ("Drowning", ["water lung", "near drowning", "swallowed water"], "Rescue breathing. Hospital checkup."),
        ("Electric Shock", ["electrocution", "shock burn", "live wire"], "Turn off power. CPR if needed."),
        ("Poisoning", ["swallowed bleach", "poison", "toxic ingestion"], "Call Poison Control immediately."),
        ("Nosebleed", ["bleeding nose", "epistaxis", "nose blood"], "Pinch soft part of nose, lean forward."),
        ("Faps", ["fainting", "passed out", "syncope"], "Legs up. Fresh air."),
        ("Shock", ["pale clammy", "in shock", "medical shock"], "Lay down, feet up, keep warm."),
        ("Concussion", ["hit head", "seeing stars", "concussion"], "Rest physically and mentally. Monitor."),
        ("Whiplash", ["neck snap", "car accident neck", "whiplash"], "Ice, rest, gentle movement."),
        ("Motion Sickness", ["car sick", "sea sick", "motion nausea"], "Look at horizon. Ginger. Meds."),
        ("Jet Lag", ["time zone tired", "jet lag", "sleep cycle"], "Sunlight exposure. Melatonin."),
        ("Hangover", ["drank too much", "hangover headache", "alcohol sick"], "Fluids, electrolytes, sleep."),
        ("Vitamin D Deficiency", ["low vit d", "bone pain", "fatigue"], "Sunlight, supplements."),
        ("Vitamin B12 Deficiency", ["nerve pain", "b12 low", "anemia b12"], "Supplements or injections."),
        ("Calcium Deficiency", ["muscle cramps", "low calcium", "hypocalcemia"], "Dairy, leafy greens, supplements."),
        ("Iron Deficiency", ["pale", "eating ice", "low iron"], "Iron supplements, meat."),
        ("Magnesium Deficiency", ["twitching", "muscle spasm", "low mag"], "Nuts, seeds, supplements."),
        ("Protein Deficiency", ["kwashiorkor", "muscle wasting", "low protein"], "High protein diet."),
        ("Scurvy", ["bleeding gums vit c", "scurvy", "vitamin c low"], "Citrus fruits."),
        ("Rickets", ["bowed legs", "soft bones", "rickets"], "Vitamin D and Calcium."),
        ("Night Blindness", ["cant see night", "vit a low", "night blind"], "Vitamin A sources."),
        ("Beriberi", ["thiamine low", "beriberi", "vit b1"], "Whole grains, supplements.")
    ]

    # Generate distinct intents for conditions
    for condition, symptoms, advice in conditions:
        tag = condition.lower().replace(" ", "_").replace("'", "").replace("-", "_")
        
        # Create variations of patterns
        item_patterns = [
            f"I have {condition}",
            f"Symptoms of {condition}",
            f"Think I have {condition}",
            f"Treatment for {condition}",
            f"What to do for {condition}"
        ]
        item_patterns.extend(symptoms)
        
        # Enhanced response templates
        item_responses = [
            f"**Possible Condition:** {condition}\n\n**Suggested Treatment:** {advice}\n\n**Note:** These are home remedies. If symptoms persist or get worse, we strongly suggest you consult a doctor for a proper check-up.",
            f"Based on your symptoms, it could be {condition}. \n\n**Treatment:** {advice}\n\n**Advice:** Please visit a doctor if this does not improve within 24 hours.",
            f"It sounds like you might be experiencing {condition}. \n\n**Remedy:** {advice}\n\n**Medical Advice:** If the condition is severe or does not subside, please see a specialist immediately."
        ]
        
        intents.append({"tag": tag, "patterns": item_patterns, "responses": item_responses})

    # 4. Fillers to reach > 200 (if needed)
    # We have ~20 Departments + 10 General + ~135 Conditions = ~165. 
    # Need ~35 more. Let's add body part pain locations.
    
    body_parts = ["Head", "Neck", "Shoulder", "Arm", "Elbow", "Wrist", "Hand", "Finger", "Thumb", "Chest", "Rib", "Stomach", "Abdomen", "Back", "Spine", "Hip", "Pelvis", "Buttock", "Leg", "Thigh", "Knee", "Calf", "Ankle", "Foot", "Toe", "Heel", "Jaw", "Tooth", "Gum", "Tongue", "Throat", "Ear", "Eye", "Nose", "Forehead", "Cheek", "Chin", "Skin", "Hair", "Nail"]
    
    for bp in body_parts:
        tag = f"pain_{bp.lower()}"
        patterns = [f"Pain in {bp}", f"My {bp} hurts", f"{bp} injury", f"Sore {bp}"]
        responses = [f"Pain in the {bp} can be due to strain or injury. Rest and monitor. If severe, see a doctor.", f"For {bp} pain, try applying a cold or warm compress depending on the type of injury."]
        intents.append({"tag": tag, "patterns": patterns, "responses": responses})

    # This pushes total to > 205.

    output = {"intents": intents}
    
    with open('intents.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Generated {len(intents)} intents.")

if __name__ == "__main__":
    generate_intents()
