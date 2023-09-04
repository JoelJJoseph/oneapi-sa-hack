from PIL import Image
import streamlit as st

# Set page configuration and styling
def app():
        
    st.markdown(
        """
    <style>
    body {
        color: #333333;
        background-color: #f7f7f7;
    }
    h1, h2, h3 {
        color: #004d80;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Main content
    st.markdown("<h1>Welcome to MediCare! 👋</h1>", unsafe_allow_html=True)




    # Display the image
    image_path = "images/brain chemistry-cuate.png"
    image = Image.open(image_path)
    resized_image = image.resize((800, 800))
    st.image(resized_image)




    st.markdown(
        """
    MediCare is your ultimate health companion, designed to empower you with knowledge and support when it comes to taking care of yourself and your loved ones. This innovative application combines two crucial features to enhance your well-being:
    """
    )


    st.markdown("## How to Keep Yourself Healthy 🌱")
    healthy_tips = [
        "Stay Active: Engage in regular physical activity to promote blood flow to the brain.",
        "Eat a Balanced Diet: Consume a diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats.",
        "Stay Mentally Active: Challenge your brain with puzzles, reading, learning new skills, and staying curious.",
        "Get Quality Sleep: Aim for 7-9 hours of restful sleep each night.",
        "Manage Stress: Practice relaxation techniques like meditation and deep breathing.",
    ]

    st.markdown("🌟 Here are some tips to maintain a healthy lifestyle:")
    for tip in healthy_tips:
        st.markdown(f"🔹 {tip}")

    # Habits to Avoid for Brain Health
    st.markdown("## Habits to Avoid for Better Health 🚫")
    unhealthy_habits = [
        "Excessive Sugar Intake: High sugar consumption can impair cognitive function over time.",
        "Sedentary Lifestyle: Lack of physical activity can negatively impact brain health.",
        "Smoking: Smoking is linked to cognitive decline and increased risk of brain-related disorders.",
        "Excessive Alcohol Consumption: Heavy drinking can damage brain cells and impair cognitive function.",
        "Poor Sleep Habits: Inadequate sleep can affect memory, concentration, and overall brain health.",
    ]

    st.markdown("🚫 Avoid these habits for a healthier life:")
    for habit in unhealthy_habits:
        st.markdown(f"🔹 {habit}")

    # Brain-Related Conditions
    st.markdown("## Health-Related Conditions 🫀🫁🧠")
    health_conditions = [
        "Chronic Diseases: Long-term neglect of health can increase the risk of chronic conditions like heart disease, diabetes, and hypertension..",
        "Obesity: Poor dietary habits and a sedentary lifestyle can lead to obesity, which is associated with numerous health problems, including type 2 diabetes, joint issues, and cardiovascular diseases.",
        "Stroke: A sudden disruption of blood flow to the brain, resulting in damage to brain tissue.",
        "Depression and Anxiety: Mental health conditions that can impact brain function and overall well-being.",
    ]

    st.markdown("🧠 Learn about these health-related conditions:")
    for condition in health_conditions:
        st.markdown(f"🔹 {condition}")

    # Benefits of Brain Health
    st.markdown("## Benefits of Better Health 🌈")
    health_benefits = [
        "Enhanced Cognitive Function: A healthy brain supports better memory, focus, and decision-making.",
        "Improved Mood: Brain health is closely linked to emotional well-being and mental health.",
        "Reduced Risk of Diseases: Healthy lifestyle choices can lower the risk of brain-related disorders.",
        "Higher Quality of Life: Maintaining brain health contributes to overall vitality and quality of life.",
    ]

    st.markdown("🌟 Enjoy these benefits by maintaining your health:")
    for benefit in health_benefits:
        st.markdown(f"🔹 {benefit}")

    # About Our Team
    st.markdown("## About Myself 👥")
    st.markdown(
        """
    Driven by a deep passion for learning and an unwavering determination, I aspire to become a proficient data analyst. As a dreamer who believes in the power of visualization and insights, I strive to transform my visions into tangible outcomes. With a commitment to practicality, I diligently pursue the implementation of my dreams.
    """
    )



    # Display the image
    image_path = "images/teamself.png"
    image = Image.open(image_path)

    st.image(image)


    st.markdown("## Want to connect: 🌟")
    connect = [
        "Portfolio: https://joeljjoseph.github.io/portfolio/",
        "LinkedIn: https://www.linkedin.com/in/joel-john-joseph-2b77a41a4/",
        "Github: https://github.com/JoelJJoseph",
        
    ]
    for connect in connect:
        st.markdown(f"🔹 {connect}")