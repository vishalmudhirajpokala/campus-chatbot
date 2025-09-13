import streamlit as st
import time
import random

# Configure the page
st.set_page_config(
    page_title="CampusBuddy - Your Campus Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# STUNNING VIBRANT CSS - HACKATHON WINNING DESIGN
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main app background - VIBRANT GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main content container - GLASSMORPHISM EFFECT */
    .main .block-container {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* ANIMATED HEADER */
    .main-header {
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
        background-size: 400% 400%;
        animation: gradientShift 3s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-family: 'Poppins', sans-serif;
    }
    
    .subtitle {
        text-align: center;
        color: #2d3748;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    /* VIBRANT SIDEBAR */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        border-right: 3px solid rgba(255, 255, 255, 0.3);
    }
    
    .sidebar-header {
        background: rgba(255, 255, 255, 0.95);
        color: #4c51bf;
        font-size: 1.5rem;
        font-weight: 700;
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.5);
    }
    
    /* FEATURE BOXES WITH NEON GLOW */
    .feature-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.7) 100%);
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: #2d3748;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-left: 5px solid #ff6b6b;
        border-right: 5px solid #4ecdc4;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .feature-box:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border-left: 5px solid #4ecdc4;
        border-right: 5px solid #ff6b6b;
    }
    
    /* PRO TIP BOXES */
    .pro-tip-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.8) 100%);
        padding: 1.5rem;
        border-radius: 20px;
        color: #2d3748;
        margin: 1rem 0;
        font-weight: 500;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 2px solid rgba(255,255,255,0.5);
        backdrop-filter: blur(15px);
    }
    
    /* CHAT MESSAGES - FIXED CONTRAST */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #1a1a1a !important;
        border-radius: 25px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255,255,255,0.5);
        font-weight: 500;
    }
    
    /* ALL TEXT IN CHAT MESSAGES */
    .stChatMessage * {
        color: #1a1a1a !important;
    }
    
    /* USER MESSAGE - BLUE WITH WHITE TEXT */
    [data-testid="stChatMessage"] .stChatMessage:has([data-testid="user"]) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        margin-left: 2rem;
    }
    
    [data-testid="stChatMessage"] .stChatMessage:has([data-testid="user"]) * {
        color: white !important;
    }
    
    /* ASSISTANT MESSAGE - WHITE BACKGROUND, DARK TEXT */
    div[data-testid="stChatMessage"]:nth-of-type(odd) {
        background: rgba(255, 255, 255, 0.95) !important;
        border-left: 5px solid #ff6b6b;
        border-right: 5px solid #4ecdc4;
        margin-right: 2rem;
    }
    
    div[data-testid="stChatMessage"]:nth-of-type(odd) * {
        color: #1a1a1a !important;
    }
    
    /* USER MESSAGE - BLUE BACKGROUND */
    div[data-testid="stChatMessage"]:nth-of-type(even) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        margin-left: 2rem;
    }
    
    div[data-testid="stChatMessage"]:nth-of-type(even) * {
        color: white !important;
    }
    
    /* CHAT INPUT - GLOWING INPUT */
    .stChatInput input {
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid #667eea;
        border-radius: 25px;
        padding: 15px 20px;
        font-size: 1.1rem;
        color: #2d3748;
        backdrop-filter: blur(10px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stChatInput input:focus {
        border: 2px solid #f093fb;
        box-shadow: 0 0 20px rgba(240, 147, 251, 0.4);
        outline: none;
    }
    
    /* BUTTONS - GRADIENT MAGIC */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    /* STATUS SPINNER - COLORFUL */
    .stStatus {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        border: 2px solid #667eea;
        backdrop-filter: blur(10px);
    }
    
    /* SIDEBAR TEXT - WHITE AND READABLE */
    .css-1d391kg .markdown-text-container {
        color: white;
        font-weight: 500;
    }
    
    .css-1d391kg h3, .css-1d391kg strong {
        color: white;
        font-weight: 700;
    }
    
    /* BALLOONS EFFECT ENHANCEMENT */
    .stBalloons {
        z-index: 999;
    }
    
    /* MAKE EVERYTHING POP */
    * {
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Comprehensive Campus Knowledge Base - Simulated Database
campus_knowledge_base = {
    "dining": {
        "main_hall": {
            "hours": "Monday-Sunday: 7:00 AM - 9:00 PM",
            "menu": "Full buffet with international cuisines, salad bar, grill station",
            "location": "Student Center, Ground Floor",
            "payment": "Meal plans, cash, and card accepted"
        },
        "cafe_blue": {
            "hours": "Monday-Friday: 6:30 AM - 10:00 PM, Weekends: 8:00 AM - 8:00 PM",
            "menu": "Coffee, pastries, sandwiches, light meals",
            "location": "Library Building, 2nd Floor",
            "specials": "Happy hour 3-5 PM: 20% off all drinks"
        },
        "food_truck": {
            "hours": "Monday-Friday: 11:00 AM - 3:00 PM",
            "menu": "Tacos, burgers, wraps, fresh smoothies",
            "location": "Main Quad (weather permitting)",
            "special": "Taco Tuesday - $2 tacos!"
        }
    },
    "library": {
        "hours": "Monday-Thursday: 7:00 AM - Midnight, Friday: 7:00 AM - 10:00 PM, Saturday: 9:00 AM - 10:00 PM, Sunday: 10:00 AM - Midnight",
        "study_rooms": "24 group study rooms available for booking",
        "booking": "Reserve online at library.campus.edu/booking or use the LibCal app",
        "floors": "5 floors: Ground (reference), 1st (computers), 2nd-4th (quiet study), 5th (group work)",
        "services": "Research help, printing, scanning, laptop checkout",
        "contact": "Reference desk: (555) 123-BOOK"
    },
    "schedules": {
        "semester_dates": {
            "fall": "August 28 - December 15",
            "spring": "January 15 - May 10",
            "summer": "May 20 - August 10"
        },
        "registration": {
            "fall": "March 15 - April 30",
            "spring": "October 15 - November 30",
            "summer": "February 15 - March 30"
        },
        "finals": {
            "fall": "December 9-15",
            "spring": "May 4-10",
            "summer": "August 4-8"
        },
        "breaks": {
            "thanksgiving": "November 23-29",
            "winter": "December 16 - January 14",
            "spring_break": "March 11-17"
        }
    },
    "facilities": {
        "gym": {
            "hours": "Monday-Friday: 5:00 AM - 11:00 PM, Weekends: 7:00 AM - 9:00 PM",
            "equipment": "Cardio machines, weight training, pool, basketball courts",
            "classes": "Yoga, Zumba, Spin, CrossFit - check schedule online",
            "location": "Athletic Complex, Building A"
        },
        "student_center": {
            "hours": "24/7 access with student ID",
            "amenities": "Study lounges, game room, post office, ATM",
            "events": "Check the events calendar for weekly activities"
        },
        "health_center": {
            "hours": "Monday-Friday: 8:00 AM - 5:00 PM",
            "services": "Basic healthcare, counseling, pharmacy",
            "emergency": "24/7 emergency line: (555) 123-HELP"
        }
    },
    "admissions": {
        "procedure": "Apply online at admissions.campus.edu",
        "deadlines": {
            "early_decision": "November 15",
            "regular_decision": "January 15",
            "transfer": "March 1"
        },
        "requirements": "Transcripts, SAT/ACT scores, 2 recommendation letters, personal essay",
        "contact": "admissions@campus.edu or (555) 123-ADMIT",
        "tours": "Campus tours available Monday-Friday at 10 AM and 2 PM"
    },
    "parking": {
        "student_lots": "Lots A, B, C require valid student parking permit",
        "visitor_parking": "Visitor lot near main entrance - $5/day",
        "permits": "Purchase at campus.edu/parking - $150/semester",
        "hours": "Enforcement Monday-Friday 7 AM - 5 PM"
    },
    "technology": {
        "wifi": "CampusNet - Use student credentials to connect",
        "computer_labs": "Available in Library (1st floor) and Tech Center",
        "help_desk": "IT support: (555) 123-TECH or helpdesk@campus.edu",
        "software": "Free Microsoft Office, Adobe Creative Suite for students"
    }
}

def analyze_query_intent(query):
    """Analyze user query to determine intent and extract relevant keywords"""
    query_lower = query.lower()
    
    # Intent mapping with keywords
    intent_keywords = {
        "dining": ["food", "eat", "dining", "restaurant", "cafe", "lunch", "dinner", "breakfast", "hungry", "menu"],
        "library": ["library", "book", "study", "research", "quiet", "study room", "computer"],
        "schedules": ["schedule", "semester", "finals", "registration", "break", "calendar", "dates"],
        "facilities": ["gym", "health", "student center", "pool", "workout", "basketball"],
        "admissions": ["admission", "apply", "application", "tour", "visit", "requirements"],
        "parking": ["park", "parking", "car", "permit", "lot"],
        "technology": ["wifi", "computer", "tech", "software", "internet", "help desk"]
    }
    
    for intent, keywords in intent_keywords.items():
        if any(keyword in query_lower for keyword in keywords):
            return intent
    
    return "general"

def get_response(user_query, knowledge_base):
    """Generate AI response based on user query and knowledge base"""
    intent = analyze_query_intent(user_query)
    
    # Enthusiastic responses with personality
    responses = {
        "dining": [
            "🍕 Time to fuel up! Here's what our amazing dining options have to offer:",
            "🥗 Hungry? You've come to the right campus guide! Let me dish out the details:",
            "🍽️ Food is the fuel of champions! Here's your dining intel:"
        ],
        "library": [
            "📚 The temple of knowledge awaits! Here's everything about our fantastic library:",
            "🦉 Wisdom seekers unite! Our library is absolutely incredible:",
            "📖 Ready to become a scholar? Here's your library guide:"
        ],
        "schedules": [
            "📅 Time management is key to success! Here's your schedule info:",
            "⏰ Planning ahead like a true champion! Here are the important dates:",
            "🗓️ Stay organized and conquer the semester! Here's what you need to know:"
        ],
        "facilities": [
            "🏋️ Our campus facilities are world-class! Here's what we've got:",
            "🎯 Ready to explore? Our facilities will blow your mind:",
            "⭐ Campus life at its finest! Check out these amazing facilities:"
        ],
        "admissions": [
            "🎓 Welcome to your future! Here's everything about admissions:",
            "🌟 Ready to join our incredible campus family! Here's the scoop:",
            "📋 Your journey starts here! Admissions info coming right up:"
        ],
        "parking": [
            "🚗 Let's get you parked and ready to roll! Here's the parking lowdown:",
            "🅿️ No more circling around! Here's your parking guide:",
            "🚙 Park like a pro with this info:"
        ],
        "technology": [
            "💻 Tech support to the rescue! Here's everything you need to know:",
            "🔧 Stay connected and productive! Tech info coming your way:",
            "⚡ Power up your digital campus life with these details:"
        ]
    }
    
    if intent in knowledge_base:
        intro = random.choice(responses.get(intent, ["Here's what I found for you:"]))
        
        # Format the response based on the intent
        if intent == "dining":
            response = f"{intro}\n\n"
            for place, details in knowledge_base[intent].items():
                place_name = place.replace('_', ' ').title()
                response += f"**🍴 {place_name}**\n"
                response += f"⏰ Hours: {details['hours']}\n"
                response += f"🍽️ Menu: {details['menu']}\n"
                response += f"📍 Location: {details['location']}\n"
                if 'specials' in details:
                    response += f"✨ Special: {details['specials']}\n"
                if 'special' in details:
                    response += f"🌮 Special: {details['special']}\n"
                response += "\n"
            response += "Bon appétit! 😋"
            
        elif intent == "library":
            response = f"{intro}\n\n"
            response += f"⏰ **Hours:** {knowledge_base[intent]['hours']}\n\n"
            response += f"📚 **Study Rooms:** {knowledge_base[intent]['study_rooms']}\n"
            response += f"💻 **Booking:** {knowledge_base[intent]['booking']}\n\n"
            response += f"🏢 **Floor Guide:** {knowledge_base[intent]['floors']}\n\n"
            response += f"🛠️ **Services:** {knowledge_base[intent]['services']}\n\n"
            response += f"📞 **Contact:** {knowledge_base[intent]['contact']}\n\n"
            response += "Happy studying! Knowledge is power! 💪📖"
            
        elif intent == "schedules":
            response = f"{intro}\n\n"
            for category, details in knowledge_base[intent].items():
                cat_name = category.replace('_', ' ').title()
                response += f"**📅 {cat_name}:**\n"
                if isinstance(details, dict):
                    for key, value in details.items():
                        response += f"  • {key.replace('_', ' ').title()}: {value}\n"
                else:
                    response += f"  {details}\n"
                response += "\n"
            response += "Stay organized and crush this semester! 🚀"
            
        elif intent == "facilities":
            response = f"{intro}\n\n"
            for facility, details in knowledge_base[intent].items():
                facility_name = facility.replace('_', ' ').title()
                response += f"**🏛️ {facility_name}**\n"
                for key, value in details.items():
                    response += f"  • {key.replace('_', ' ').title()}: {value}\n"
                response += "\n"
            response += "Make the most of our amazing facilities! 🌟"
            
        elif intent == "admissions":
            response = f"{intro}\n\n"
            response += f"📝 **Application Process:** {knowledge_base[intent]['procedure']}\n\n"
            response += "**📅 Important Deadlines:**\n"
            for deadline, date in knowledge_base[intent]['deadlines'].items():
                response += f"  • {deadline.replace('_', ' ').title()}: {date}\n"
            response += f"\n📋 **Requirements:** {knowledge_base[intent]['requirements']}\n\n"
            response += f"📞 **Contact:** {knowledge_base[intent]['contact']}\n\n"
            response += f"🚶 **Campus Tours:** {knowledge_base[intent]['tours']}\n\n"
            response += "We can't wait to welcome you to our campus family! 🎉"
            
        elif intent == "parking":
            response = f"{intro}\n\n"
            for key, value in knowledge_base[intent].items():
                response += f"**🅿️ {key.replace('_', ' ').title()}:** {value}\n\n"
            response += "Drive safe and park smart! 🚗✨"
            
        elif intent == "technology":
            response = f"{intro}\n\n"
            for key, value in knowledge_base[intent].items():
                key_formatted = key.replace('_', ' ').title()
                response += f"**💻 {key_formatted}:** {value}\n\n"
            response += "Stay connected and tech-savvy! 🔌⚡"
            
        return response
    else:
        # Fallback for unrecognized queries
        fallback_messages = [
            "🤔 Whoops! I'm still learning about campus life! I'm your go-to guide for dining spots, library info, schedules, facilities, admissions, parking, and tech support. Try asking me about any of those topics! 🎓",
            "🌟 Hmm, that's a new one for me! But hey, I'm absolutely brilliant at helping with dining, library services, campus schedules, facilities, admissions info, parking, and technology. What would you like to know about? 🚀",
            "📚 Oops! My campus expertise covers dining, library services, academic schedules, facilities, admissions procedures, parking info, and technology support. Ask me about any of these and I'll knock your socks off with helpful info! 🎯"
        ]
        return random.choice(fallback_messages)

def main():
    # STUNNING ANIMATED HEADER
    st.markdown('<h1 class="main-header">🎓 CampusBuddy</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🌟 Your Ultimate Campus Information Companion! 🚀</p>', unsafe_allow_html=True)
    
    # VIBRANT SIDEBAR
    with st.sidebar:
        st.markdown('<div class="sidebar-header">✨ Welcome to CampusBuddy! ✨</div>', unsafe_allow_html=True)
        st.markdown("**I'm your enthusiastic campus guide, ready to make your college life AMAZING! 🎉**")
        
        st.markdown("### 🎯 **I Can Help You With:**")
        
        features = [
            "🍕 **Dining Options** - Hours, menus, locations & amazing specials!",
            "📚 **Library Services** - Hours, study rooms & all resources!", 
            "📅 **Academic Schedules** - Semesters, finals & registration dates!",
            "🏋️ **Campus Facilities** - Gym, health center & student activities!",
            "🎓 **Admissions Info** - Applications, tours & requirements!",
            "🅿️ **Parking Information** - Permits, lots & regulations!",
            "💻 **Technology Support** - WiFi, computers & software access!"
        ]
        
        for feature in features:
            st.markdown(f'<div class="feature-box">{feature}</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💡 **Pro Tips:**")
        st.markdown("""
        <div class="pro-tip-box">
        Ask me specific questions like <strong>'When is the library open?'</strong> or <strong>'Where can I get food on campus?'</strong> for the most helpful results! I love detailed questions! 🎯
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📞 **Need More Help?**")
        st.markdown("""
        <div class="pro-tip-box">
        Visit our <strong>Student Services Center</strong> or call <strong>(555) 123-HELP</strong> anytime for additional support! We're here for you 24/7! 💪
        </div>
        """, unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # EPIC WELCOME MESSAGE
        welcome_message = """🎉 **HEY THERE, SUPERSTAR!** 🎉

I'm CampusBuddy, your absolutely AMAZING virtual campus assistant! 🚀✨ 

I'm PUMPED to help you with:
🍕 Dining halls & food spots
📚 Library services & study spaces  
📅 Academic schedules & important dates
🏋️ Campus facilities & activities
🎓 Admissions & campus tours
🅿️ Parking info & permits
💻 Tech support & WiFi help

**What awesome thing can I help you discover today?** 🌟

Just ask me anything about campus life and watch the magic happen! ✨"""
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})
    
    # Display chat messages with STUNNING STYLING
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant", avatar="🎓"):
                st.markdown(message["content"])
    
    # ✅ FIXED: Chat input placed at the BOTTOM (outside any containers)
    # This is the critical fix for the StreamlitAPIException
    if prompt := st.chat_input("✨ Ask me ANYTHING about campus life! I'm ready to blow your mind! 🎓🚀"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response with EPIC EFFECTS
        with st.chat_message("assistant", avatar="🎓"):
            with st.status("🧠 **Working my MAGIC on the campus database...** ✨", expanded=False):
                time.sleep(1)
                st.write("🔍 **Analyzing your awesome question...**")
                time.sleep(0.7)
                st.write("📚 **Gathering the most AMAZING information...**")
                time.sleep(0.7)
                st.write("✨ **Preparing your PERSONALIZED response...**")
                time.sleep(0.8)
                st.write("🎉 **Almost ready to BLOW YOUR MIND!**")
                time.sleep(0.5)
            
            response = get_response(prompt, campus_knowledge_base)
            st.markdown(response)
            
            # EPIC CELEBRATION FOR POSITIVE INTERACTIONS
            if any(keyword in prompt.lower() for keyword in ["thank", "thanks", "great", "awesome", "perfect", "amazing", "love"]):
                time.sleep(1)
                st.balloons()
                st.success("🎉 You're absolutely AMAZING! Keep being awesome! 🌟")
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()