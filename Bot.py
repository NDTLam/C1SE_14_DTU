from math import e
import speech_recognition 
import pyttsx3
from datetime import date, datetime

bot_ear = speech_recognition .Recognizer()
bot_mouth = pyttsx3.init()
bot_brain = "...."

while True:
    with speech_recognition.Microphone() as mic:
        print("Bot: I'm listening to you")
        audio = bot_ear.listen(mic)
    print("Bot: ...... ")

    try:
        you = bot_ear.recognize_google(audio)
    except:
        you = ""
    print("You :"+ you) 

    if you == "":
        bot_brain = "I can't hear anything, please speak again"
    elif "hello" in you:
        bot_brain = "Hello"
    elif "today" in you:
        today = date.today()
        bot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now() 
    elif "who are you ?" in you:
        bot_brain = "I'm James,I am a tool to help you learn about Covid-19"
    
    #TÌM HIỂU CHUNG VỀ DỊCH BỆNH Covid-19   
    #1  
    elif "What is an infectious disease?" in you:
        bot_brain = "An infectious disease is a disease that is transmitted directly or indirectly from humans or from animals to humans due to pathogens.Infectious. Example: Seasonal flu is spread directly from person to person dengue fever is transmitted from person to person mosquito bites, avian flu is transmitted from birds to humans."
    #2
    elif "What is the Covid-19 epidemic?" in you:
        bot_brain = "Covid-19 is an abbreviation for the phrase 'Coronavirus disease 2019', is an epidemic caused by corona virus and appeared for the first time early 2019.This disease first appeared in Wuhan city, provinceHubei, China, in which many people have acute respiratory infections. The causative agent was then identifiedis a new strain of Corona virus. This new virus strainfound in 2019 should be denoted as 2019-nCoV (writtenabbreviation for the phrase “2019 Novel Coronavirus”). So at firstThis disease is called “Acute respiratory infection caused bynew strain of Corona virus 2019-nCoV”"
    #3
    elif "How is Covid-19 spread?" in you:
        bot_brain = "Currently, the exact mode of transmission from animals towhat kind of person is not clear; what is certain is the person (orpeople) first contracted the virus from animalshave contact with a source of virus spread by animals (substancewaste, secretions, raw meat, etc.). From these sources, the virus that causes Covid-19 has infected cells in the respiratory tract ofinfected person. Here, the virus multiplies and causes diseaserespiratory tract and spread out through the respiratory tracton an infected person and then spread it from person to personothers."
    #4
    elif "What is the causative agent of Covid-19?" in you:
        bot_brain = "The causative agent of Covid-19 is a strain of Corona virus.The virus that causes Covid-19 is different from other virusesCorona was known before, so it was named “virus”New Corona” (Novel Coronavirus - nCoV for short)."
    #5
    elif "Covid-19 epidemic compared to SARS and respiratory infectionsMiddle East (MERS), which epidemic is more dangerous?" in you:
        bot_brain = " Mortality rate: The fatality rate for SARS was 9.6%, for MERS over 30% higher than Covid-19 (currently around 2%)." 
        bot_brain = " Level of spread and number of infected people: Covid-19 has a contagious degree spread faster and more people infected. Hitherto (February 17, 2020), more than 70,000 people have been infected worldwide and more than 1,700 deaths, far exceeding the number of infections and deaths caused by SARS and MERS combined."
    #
    elif "...." in you:
        bot_brain = ""
    
    #TÁC NHÂN GÂY BỆNH 
    #1
    elif "What is the causative agent of Covid-19?" in you:
        bot_brain = "The causative agent of Covid-19 is a strain of Corona virus.The virus that causes Covid-19 is different from other virusesCorona was known before, so it was named “virus”New Corona” (Novel Coronavirus - nCoV for short)."
    #2
    elif "Where did the Covid-19 virus come from?" in you:
        bot_brain = "The name Corona originates from the virus identification feature whenseen under an electron microscope, they have protruding spines on their facesThe outside looks like a crown."
    #3
    elif "Where is the Covid-19 virus in our surroundings?" in you:
        bot_brain = "Covid-19 is a virus that is present in both humans and sick animals as well asHumans and animals that carry the virus do not show any symptoms. Are fromHumans and animals carry viruses, Covid-19 is released into the environmentThe surrounding field is mainly in the form of droplets from secretionsrespiratory tract when coughing, sneezing, blowing your nose or spitting. DropletsThis shot causes air pollution within a radius of 2m fromdispersal source. From the air, droplets fall onto the surface of theobjects such as clothes, furniture, phones, computer keyboards,elevator buttons… directly contaminate these surfaces.If someone touches the contaminated surface and then touches it againother objects such as doorknobs, elevator buttons, wallschairs, stair handrails, handrails on vehiclesvent… will continue to contaminate new surfaces indirectlythis. Thus, Covid-19 exists mainly in the air indistance within a radius of about 2m around the personcarrying the virus cough, sneeze, blow your nose without wearing a mask orcover your nose and mouth with your hand; on the surface of surrounding objectsthe area where people cough, sneeze, blow their nose, spit, and possibly onThe surface of secondary contaminated objects is difficult to identify."
    #4
    elif "Does the Covid-19 virus multiply in the natural environment?" in you:
        bot_brain = "Are not. Covid-19 in particular and viruses in general do not self-replicatecan up. Viruses must 'borrow' living cells to multiply byhow to 'control' the host cell to 'work' for the virus. Afterinfecting a virus cell will control the host cell byhow to insert viral genes into the host cell's genomeVirus-infected cells produce viral components. When it's enoughnecessary components, which are assembled witheach other to form many new viruses, and at the same time damagedamage to virus-infected cells."
    #5
    elif "How long does the Covid-19 virus survive in the natural environment?" in you:
        bot_brain = "In the natural environment, viruses only exist in their original form anddoes not multiply, so the life time of the virus in the environmentThe natural field is the lifetime of a virus generation. TimeHow long this time will depend on the nature of the virus and thenatural condition. Normally, at cold temperatures the virus willlast longer, especially in deep negative cold temperatures; other factorssuch as humidity, surface material (soil, wood, iron, etc.)to the lifetime of the virus; especially sunlight hasVery effective in killing viruses."
    #6
    elif "How does the Covid-19 virus infect humans?" in you:
        bot_brain = "Each virus has specific structures on its active surfaceact like hooks for viruses to attach to structuressuitable for that type of hook (called a receptor)on the surface of the host cell to allow the virus to enter the cell. TeeWhich cell has a structure that allows the 'hooks' of the virus to 'hook' in? The cells will be 'sensitive' to the virus and infected by the virus."
    #7
    elif "What is direct contact with sick people?" in you:
        bot_brain = "Is “skin-to-skin” contact, kissing, or sexual intercourse withpatient. Direct contact with blood and body secretionsPatients are considered to be in direct contact with the pathogen."
    #8
    elif "What is close contact with sick people?" in you:
        bot_brain = "Being in contact with the patient within a distance of 2m or being in the same rooma room or area where a confirmed case is taken care of forpredisposition to illness or the likelihood of being ill for a long time."
    #9
    elif "Does shaking hands spread Covid-19?" in you:
        bot_brain = "Are not. So far there is no evidence that the Covid-19 virus hascan enter the body through the skin. However, shaking hands is an acthigh-risk activity. When a person's hand is infected with Covid-19Touching someone else's hand can transmit the virus to someone's handthis. The virus can be transmitted from the hands to the respiratory tractdue to other actions such as rubbing your eyes, picking your nose, raising your handsmouth or even touching your face, giving you the opportunity (no matter how small) toThe virus 'flys' into the nose. So practice hand washing/hand sanitizerand don't touch your face (especially after shaking hands)It is an effective measure to prevent the risk of infection by shaking hands."
    #10
    elif "Kissing can spread Covid-19?" in you:
        bot_brain = "Yes. When kissing, whether it's a kiss on the lips or a kiss on the forehead or on the cheek, it's still the samedirect contact with the patient."
    #11
    elif "Can sexual activity spread Covid-19?" in you:
        bot_brain = "There is no research to prove that Covid-19 can be transmitted through mucous membranesGenital tract or not and therefore sexually transmitted?heterosexual intercourse or not. However, because sexual activity has many forms, levels and movementsTherefore, sexual activity is a risky behavior. RiskThe chance of getting infected is high or low depending on the degree of interaction betweensexual partners exposed to respiratory secretions ofpeople with Covid-19. When things are not clear, do itSafe sex behaviors to both protect peoplealready infected with Covid-19 before the risk of being infected with more infectious diseasessexually transmitted, while protecting your partner from infectioninfected with Covid-19 from a previously infected person."
    #12
    elif "Is Covid-19 spread through food?" in you:
        bot_brain ="There is no research to prove that Covid-19 can be transmitted through sexual contacteat or not. Although there are studies that showCovid-19 in the stool of patients and some patients havepresenting with diarrhea, which suggests that Covid-19 may causegastrointestinal damage. Because the mouth and nose are connectedso it's not known whether the virus fell from the respiratory tract into the roadDigestion and excretion of feces or viruses from food in the mouthwork on the respiratory tract. When all possibilities cannot be ruled outYou should still practice 'eating cooked, drinking boiling' to preventTranslate. Absolutely do not eat raw blood pudding, raw meat - mostof wild animals."
    #13
    elif "Is Covid-19 spread through blood?" in you:
        bot_brain = "There is no information on this issue. From a backup point of view,Covid-19 is a particularly dangerous infectious diseaseRecommendations on the protection of health workers are all set tohighest risk of exposure to the patient's blood.In terms of blood transfusion safety, in the current period, it is certain that people who test positive for Covid-19 will not be able to donate blood voluntarily in mass voluntary blood donations. In the future, whether the Covid-19 test will be included in the blood transfusion safety screening test group, it is still waiting for more solid evidence on whether the virus is transmitted through blood."
    #14
    elif "Is Covid-19 transmitted from mother to child?" in you:
        bot_brain = "During this epidemic, Chinese scientists have been monitoring9 cases of pregnant women infected with Covid-19 and gave birthchild. Tests of amniotic fluid, umbilical cord blood of newborns born to mothersinfected with Covid-19 and breast milk did not show Covid-19 virus.More information on non-communicable SARS-CoV and MERS-CoVVertical transmission from mother to child makes scientists temporarilyconcluded that Covid-19 is not vertically transmitted from mother to child.Even so, the observations were made only in 9 cases, soMore people's data is needed to draw a firm conclusionsure about this.Note: Vertical transmission is understood as transmission from mother to child throughplacenta. Isolate the child from the mother to avoid transmission throughinhalation or direct contact is still necessary."
    #15
    elif "How does the Covid-19 virus cause disease?" in you:
        bot_brain = "After infecting the cells of the respiratory tract mucosa,Covid-19 inserts viral genes into the host cell's genome, startingVirus-infected cells produce viral components. Onceall the necessary components, these components put togethertogether to form many new viruses that come out (photoside) and at the same time damage virus-infected cells.The sequence of steps includes: Translation of the copied gene from RNAvirion genes. They first synthesize the RNA strandS, E, and M viral structural proteins are transferred to the endoplasmic reticulum(ER) and migrate into the reticulum-Golgi . medial compartment(ERGIC) Nucleocapsid mature virion particles (ieare new viruses). New viruses form and continue to spread"
    #16
    elif "Is Covid-19 teratogenic?" in you:
        bot_brain = "It is not yet possible to answer whether Covid-19 can cause any effectto the fetus. In fact, it is necessary to long-term follow-up of pregnancy consequencesproduct of patients who are pregnant womenCovid-19 infection in the early stages of pregnancy."
    #
    elif "...." in you:
        bot_brain = ""

    #PHÒNG CHỐNG DỊCH 
    #1
    elif "Why are some people infected with Covid-19 getting sick, others not getting sick?" in you:
        bot_brain = "When infected with a pathogen, whether or not a person gets sick will depend on factors from the pathogen and factors from the person infected with the pathogen. Being sick or not is the result ofwar between pathogens and humans, if pathogensIf you win, that person will get sick. The same person but ifInfection with low viral load and low virulence may result indo not develop disease; the same amount of virus but the ability toAntiviral resistance of each person is different, in which peoplehave good resistance can not get sick. So next toProtecting yourself to limit the spread of pathogens, exercisingIncreases general resistance also contributes to preventiondiseases - especially infections."
    #2
    elif "Does anyone have natural resistance to Covid-19?" in you:
        bot_brain = "Absolutely possible. People with mutations in the gene that encodesVirus receptor makes it impossible for the virus to enterinside the cell is a person with a natural resistance tovirus. This has been confirmed in the case of HIV.However, it is too early to find out who has natural resistancewith Covid-19. Hope the technology to decode the human genome is nowhas now been developed to allow whole-genome sequencingpeople in a short time and low cost will facilitatescreening among those infected or exposed toCovid-19 but not sick to. That way it might befind people with genetic mutations that make it possible tonatural resistance to Covid-19."
    #3
    elif "How is the human body resistant to Covid-19?" in you:
        bot_brain = "Is a completely new virus, appearing in humans for the first timeso no one has specific resistance to the virus. So the bodyPeople newly infected with Covid-19 for the first time will be resistant toviruses by non-specific natural meansanterior (mainly chemical elements in mucosal secretions)respiratory tract). If this mechanism wins, then that personnot sick. If this mechanism fails, the person is infectedpathogens inside cells. At this time, the system is freebody fluids of infected people will develop mechanisms to preventspecific resistance to eliminate the virus and also infected cellsvirus. This is a race between destructive attack power on the one handthe destruction of the virus with one side being the body's resistance to controlvirus replication and elimination plus the ability to replicatecells that have been damaged by the virus. If the virus wins, the disease willprogression, if the immune system wins, the patient is cured."
    #4
    elif "How long after being infected with Covid-19 will have antibodies?" in you:
        bot_brain = "This process takes at least 1 week or somore from person to person, similar to the time since injectionvaccine until the onset of specific antibodies.This period is often referred to as the 'window period'from the time the pathogen is infected until it can be indirectly detectedInfection with pathogens through testing for antibodies thatcreated to fight off the infected pathogen.Currently testing for IgM antibodies against Covid-19has also begun to be applied to detect infected peopleCovid-19. However, this is only circumstantial evidenceThis test has the disadvantage that it has to go through the 'window period' before it can be detected."
    #5
    elif "People who got sick from Covid-19 once and got sick againthis anymore?" in you:
        bot_brain = "May or may not be subject to certain conditions. IfCovid-19 creates lasting immunity like measles virus ormumps does not come back; However, this cannot be confirmeddetermined because it is too early. If immunity is not sustained,In the early stages of recovery, the amount of antibodies is strong enoughthen it may not come back, but in the later stages of resistanceThe specific body gradually disappears, but it can still come back. In schoolsIn this case, vaccines should be used to restore immunityantiviral resistance."
    #6
    elif "Is there currently a vaccine for Covid-19?" in you:
        bot_brain = "Already, vaccine intended to provide acquired immunity against coronavirus 2 with severe acute respiratory syndrome (SARS‑CoV‑2), the virus that causes coronavirus disease 2019 (COVID‑19). Prior to the COVID-19 pandemic, an established body of knowledge existed about the structure and function of coronaviruses that cause diseases such as severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (SARS). MERS). This knowledge spurred the development of various vaccine technologies in early 2020. On January 10, 2020, SARS-CoV-2 genetic sequence data was shared through GISAID, and On March 19, 2020, the global pharmaceutical industry announced a fundamental commitment to tackle COVID-19. COVID-19 vaccines are widely recognized for their role in reducing the spread, severity, and deaths caused by COVID-19."
    #
    elif "...." in you:
        bot_brain = ""

    #VỀ BỆNH 
    #1
    elif "What are the symptoms of people with Covid-19?" in you:
        bot_brain = "Common initial clinical symptoms are fever, dry cough,fatigue, muscle pain. In some cases there may be a sore throat,stuffy nose, runny nose, headache, cough with phlegm, vomiting and diarrhearun. Severe cases appear pneumonia; shortness of breathdue to severe pneumonia, acute respiratory distress syndrome (ARDS); organ failure. Symptoms of the diseaseappear 2-14 days after exposure to the source of the disease."
    #2
    elif "Being infected with Covid-19 if not treated can lead toWhat are the consequences?" in you:
        bot_brain = "People infected with Covid-19 can progress to different degreeseach other, mild can be self-healing, severe can progress to inflammationSevere pulmonary disease, progressive acute respiratory failure, muscle dysfunctionrelated to death. According to currently published data, the ratemortality is about 2%. Severe disease often occurspresent in people with chronic diseases, immunocompromised."
    #3
    elif "Is it true that every cough and fever is a disease caused by Covid-19?" in you:
        bot_brain = "Is it true that every cough and fever is a disease caused by Covid-19?Cough, fever are manifestations of many different acute and chronic diseases related to the respiratory tract. Disease caused by Covid-19 is aacute respiratory disease. There are many possible causescause acute respiratory infections such as bacteria that causesick; viruses such as seasonal influenza viruses, parainfluenza viruses, respiratory virusessyncytiocytosis… Therefore, not every cough and fever are symptomscurrently ill with Covid-19.The patient has a cough and fever and has come to, stayed at, and returned from an epidemic area, orbeen in contact with a person suspected of being infected with Covid-19 within 14 daysshould immediately go to the nearest medical facility for advice, examination and treatmentTests to diagnose Covid-19?"
    #4
    elif "What tests should be done to confirm that I have Covid-19 disease?" in you:
        bot_brain = "According to the current regulations of the Ministry of Health, the test confirmsdefinitely get sick from Covid-19 conducted at medical facilitiespermitted by the Ministry of Health to conduct and publish the test resultsexperience. Currently, techniques to identify Covid-19 include:Next-generation gene sequencing (NGS) and Real time RT-PCRwith specimens as respiratory tract fluid, sputum, endotracheal fluidcollected and stored in a suitable environment."
    #5
    elif "Is there currently a specific treatment for Covid-19?" in you:
        bot_brain = "Currently, the World Health Organization and other health organizations have notAre there any specific drug recommendations for pneumonia caused byCovid-19. Several antiviral drugs are being studied forefficacy and safety for Covid-19 patients."
    #6
    elif "What are the current main measures to treat illness caused by Covid-19?" in you:
        bot_brain = "Because there is no specific treatment drug, supportive treatmentSupporting physical condition, resistance and treating symptoms is key. It is necessary to monitor and detect early and promptly handle casessevere, critical illness such as respiratory failure or other organ failure."
    #
    elif "...." in you:
        bot_brain = ""
        
    #BIỆN PHÁP PHÒNG BỆNH    
    #CÁCH LY 
    #1
    elif "What is medical isolation?" in you:
        bot_brain = "Medical isolation is the separation of people with infectious diseases,a person suspected of having an infectious disease, a carrier of an infectious disease or an object capable of carrying an infectious agent in order to limit the transmission of the disease."
    #2
    elif "Why is it necessary to conduct medical isolation during the Covid-19 epidemic?" in you:
        bot_brain = "According to the Law on Prevention and Control of Infectious Diseases in 2007,Covid-19 is a particularly dangerous infectious disease, so it is imperative to carry out medical isolation measures."
    #3
    elif "What forms of medical isolation are there?" in you:
        bot_brain = "Isolation at home and place of residence: Applied to common epidemic diseasesUsually, there is little risk of serious health consequencescommunity health"
        bot_brain = "Isolation at medical examination and treatment establishments (hospitals):used with high-risk diseases, causing serious consequencesimportant to public healthIsolation at medical examination and treatment establishments (hospitals):used with high-risk diseases, causing serious consequencesimportant to public health"
        bot_brain = "Strict isolation: Is the highest form of isolation 'internal'export - foreign import'. That means the person is in the quarantine areastrictly, do not leave the isolation area untilwhen there is a decision to end the isolation of the competent authority. In contrast, people who are outside the area are also notadmitted until the end of the quarantine."
    #4
    elif "What is centralized medical isolation?" in you:
        bot_brain = "Centralized medical isolation is when a group of people are at risk of infectiondisease (for example: This group of people has just returned from an epidemic area) are gathered in one area (maybe a military barracks).team, field hospital...) for isolation according to regulations."
    #5
    elif "What is self-isolation?" in you:
        bot_brain = "Self-isolation is self-isolation of an individual suspected of having a contagious diseaseinfected but have no symptoms of illness or have been testedtest negative for pathogens but suspicion is not realTo limit the possibility of infection, actively isolate yourself to limitinhibit disease transmission."
    #6 
    elif "Do people returning from epidemic areas on duty have to undergo isolation?" in you:
        bot_brain = "Persons assigned to duty where there aretranslators (such as healthcare workers or payroll workers)food, food and medicine for epidemic areas…) often havehave secured means of personal protection and have beenwell trained in epidemic prevention measures. ActiveThis action is carried out according to strict proceduresand closely monitored. Depending on the level of work ofthat person, as well as manipulating epidemic prevention techniquesthat person performs…, the authorities will decideisolation level of these people."
    elif "...." in you:
        bot_brain = ""

    #SỬ DỤNG KHẨU TRANG 
    #1
    elif "Why can wearing a mask prevent respiratory infections?" in you:
        bot_brain = "Masks when used with the right type and in the right way workprevent pathogens from the respiratory tract ofdisease carriers spread to the air and from the airinto the respiratory tract of an uninfected person. Effectiveprevention is higher when both the carrier and theNon-carriers use masks."
    #2
    elif "How many types of medical masks, basic structure and workuse of each type?" in you:
        bot_brain = "Medical masks have two types: surgical masks and surgical maskspage with high filtering effect."
        bot_brain = "How many types of medical masks, basic structure and workuse of each type?Medical masks have two types: surgical masks and surgical maskspage with high filtering effect.Surgical masks only prevent large droplets of 5 micrometers or more and are transmitted within 1m when coughing, sneezing, aspirating sputum ..."
        bot_brain = "High-strength masks (N95, N96, N99...) prevent respiratory transmission through droplets below 5 micrometers."
    #3
    elif "Is wearing a mask to protect someone who has not been infected or to protect someone who has been infected with Covid-19?" in you:
        bot_brain = "Wearing a mask has a dual effect to protect people who have not yet been infectedinfected and infected people. Both of these purposes are importantimportant. The preventive effect will be higher when the whole person is carryingpathogens and non-carriers used togethermasks, especially during a respiratory epidemicAs hot as the Covid-19 epidemic"
    #4
    elif "What is the correct way to wear a medical mask?" in you:
        bot_brain = "When wearing, make sure your hands are clean, always wear the waterproof face outside, adjust the metal bar to hug the nose and the strap firmly. The mask must cover the nose and mouth. Do not touch the outside surface during use. When removing, wash your hands, remove the strap with your hands and just put the strap in the trash, do not touch the outside of the mask. The time to wear a disposable mask is about 6-8 hours."
    #5
    elif "When to wear a mask?" in you:
        bot_brain = "People need to wear medical masks in the following cases: When there are respiratory symptoms such as cough, difficulty breathing; upon contact,taking care of people infected/suspected of being infected with Covid-19; when taking care of or being in close contact with someone who has symptoms of coughing, sneezing, runny nose, difficulty breathing or is assigned to self-monitor, isolate at home or when going to a medical facility."
    #6
    elif "...." in you:
        bot_brain = ""
    
    #RỬA TAY 
    #1
    elif "Covid-19 is a respiratory virus, why does hand washing limit the spread of pathogens?" in you:
        bot_brain = "Human hands are the part that comes into contact with surrounding objectsthe most (holding, grasping, touching ...), so there is also a high risk of gettingcontamination with agents (be it bacteria, viruses, etc.) from items.When holding utensils to eat, or wipe your face, or make movementsSimilarly, putting it on your face easily increases the risk of Covid-19 infection(through respiratory mucosa, eye mucosa, etc.).Hand washing reduces or even eliminates pathogens on infected handspollution should limit the risk of disease transmissiongeneral and Covid-19 in particular."
    #2
    elif "When should we wash our hands to limit the spread of Covid-19?" in you:
        bot_brain = "Any time there is a risk of hand contamination, especially after hand touchingcover your nose and mouth when coughing or sneezing; after touching, holding, grasping thesurrounding objects. In areas where there are suspected infected people or contact with suspected people with symptoms such as coughing, sneezing, fever, etc., it is necessary to carry out regular hand washing measures.more often. In addition, you should wash your hands before and after eating, after going to the toilet, after preparing food, etc. It is necessary to practice frequent hand washing habits, even if not during the Covid-19 epidemic, to prevent many diseases. other communicable diseases caused by contaminated hands"
    #3
    elif "Why wash hands with soap?" in you:
        bot_brain = "Washing hands with clean water reduces agents such as bacteria,virus... Soap is a compound containing esterified fatty acids andSodium hydroxide or potassium hydroxide has detergent properties. Ask for a favordetergent contained in the composition that soap hascleaning feature. These cleaners have surface tensionLarge surface, effective in removing dirt and organic matter on"
    #4
    elif "What is dry hand washing?" in you:
        bot_brain = "Dry hand washing is a method of disinfecting hands with a solutionSpecialized hand washing without rinsing with water. Dry hand sanitizers often contain alcohol, after disinfecting handsAlcohol evaporates so hands are dry again without wiping or drying"
    
    #VỆ SINH, DINH DƯỠNG 
    #1
    elif "Why is it important to clean the environment to limit the spread of Covid19?" in you:
        bot_brain = "The environment is considered as the 'home' of pathogenssick. Clean environment makes pathogensdisease in general, the Covid-19 virus in particular has no 'home' due toThat limits the infection."
    #2
    elif "How should the environment be cleaned to limit the spread of Covid-19?" in you:
        bot_brain = "The environment needs to be clean. If there is sunshineSunlight will have a very effective effect on killing viruses. When necessary, in addition to general cleaning, it is necessary to apply disinfectant to kill the Covid-19 virus."
    #3
    elif "How to clean the house to limit the spread of Covid-19?" in you:
        bot_brain = "The house (house, office, etc.) is the environment where peoplelive and work and there is also the risk of Covid19 contamination. Because Covid-19 is in the air and especially surfacesShould the house be cleaned to reduce the risk of pollution?air and surface pollution. The house should be well ventilated; limited ordo not use air conditioning because it does not stagnate in the house;If possible, open the door to allow air circulation.Sweep and clean the house regularly. Especially when there isSunlight should open the door for ventilation and sunlightThe sun shining in the house has the effect of killing viruses."
    #4
    elif "What items need to be cleaned regularly to limit the spread of Covid-19?" in you:
        bot_brain = "Items that need regular cleaning to limit the spread of Covid-19 are objects with a high risk of contamination such as objects used by many people: Door handles, elevator buttons, stair handrails, etc. shared phone buttons, shared table tops… even cash flows from one person to another; 's objectsindividuals but with high frequency of contact with hands or face areas such as mobile phones, computer keyboards, facedesk…"
    #5
    elif "How to properly clean objects and the environment?" in you:
        bot_brain = "Items that need to be cleaned regularly with solventsDisinfectant such as soap, alcohol solution orchloramine. With the external environment, hygiene measures are clean,good water, clear bushes…; If contamination is suspected, it is necessaryDisinfectant spray with 0.2% chloramine solution of active chlorine.If you are in a place where there are already suspected Covid-19 patients, spraysolution containing 0.5% active chlorine"
    #6
    elif "What detergents are often used to clean objects and the environment to prevent Covid-19 infection?" in you:
        bot_brain = "Only cleaning agents containing oxidizing agents or alcohol are effectivedestroy this pathogen. The most commonly used oxidizing agentnow chloramine."
    #7
    elif "Why is it important to keep the body warm to prevent the spread of Covid-19?" in you:
        bot_brain = "Between body warmth helps the body's general resistance be better. Some organs when cold can lead to infections such as pharyngitis, bronchitis, pneumonia ... will doincreased risk of Covid-19 infection; At the same time, if infected with more Covid-19 will be at risk of making the disease worse."
    #8 
    elif "How should the diet be maintained to increase resistance against Covid-19?" in you:
        bot_brain = "There is no specific diet to increase resistance toCovid-19.You should maintain a reasonable, nutritious, and nutritious dietVitamin supplements to increase general resistance. Since the possibility of food-borne transmission has not been ruled out, 'eating cooked and drinking boiling' should be carried out. Absolutely do not eat raw food such as blood pudding, raw meat"
    #9 
    elif "How to prepare mentally to overcome the Covid-19 pandemic?" in you:
        bot_brain = "Psychological work should be prepared even for those who have been infectedCovid-19 as well as uninfected people; psychology for the individualand for the community."    


    elif "bye" in you:
        bot_brain = "Goodbye"
        print("Bot: " + bot_brain)
        bot_mouth.say(bot_brain)
        bot_mouth.runAndWait()
        break
        
    else:
        bot_brain = "I'm fine thank you"


    print("Bot: " + bot_brain)
    bot_mouth.say(bot_brain)
    bot_mouth.runAndWait()
