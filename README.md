# oneapi-sa-hack

#### Project Name - MediCare
#### AI Super Reference Kit- Voice Data Generation and Disease Prediction Using NLP
#### Email - joeljoseph1810@gmail.com
#### Website link - https://oneapi-sa-hack.streamlit.app/
## DEMO VIDEO - https://youtu.be/bGZvwvAWdiI
#### Prototype Link: https://oneapi-sa-hack.streamlit.app/

## Inspiration<img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/0237fb2a-7625-422b-9346-6aace1656d8f" height="80" width="80"><br>
In a world marked by evolving healthcare challenges and disparities, my project emerges as a beacon of innovation and compassion. I have witnessed the ever-increasing complexity of healthcare systems, the pressing need for accessible medical information, and the desire for personalized health solutions. In this landscape, my project was born with a mission: to bridge these gaps and empower individuals with the knowledge and support they need for a healthier life. In today's world, where reliable healthcare resources are often inaccessible, and navigating medical decisions can be overwhelming, my project stands as a solution that brings simplicity, accessibility, and informed decision-making to the forefront. I have tackled the challenges of data privacy, information overload, and diverse user needs head-on, driven by the belief that everyone deserves easy access to healthcare information and personalized recommendations. My project is not just about technology; it's about enhancing lives, fostering health equity, and envisioning a brighter and healthier future for all.
## A Brief of the Prototype <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/873a5645-68ca-4847-b86b-0b158fdd3d82" height="80" width="80"> <br>

The project MediCare has harnessed the power of artificial intelligence to revolutionize healthcare support. One pivotal tool that played a crucial role in achieving our mission was the AI Reference Kit Library. This comprehensive library provided us with a robust foundation for implementing AI-driven features such as the intelligent chatbot for first-aid assistance and the predictive medicine recommendation system
<h2>Introducing MediCare</h2>
<img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/8af5d79d-c63c-4409-8b8d-684133a937d3" alt="Homepage" height="500">


## Features we Offer <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/16251a52-624d-4c5d-85f9-ee8c4991e00f" height="80" width="80"> <br>
⭐ First-Aid Assistance: Instant guidance for emergency first-aid situations.<br>
⭐ Medicine Recommendations: Personalized advice for managing health concerns. <br>
⭐ Health Information Hub: Reliable resources for informed decisions. <br>
⭐ Preventive Tips: Lifestyle guidance to reduce health risks. <br>
⭐User-Friendly Interface: Easy navigation for all ages. <br>
⭐AI-Powered Support: Smart responses and accurate recommendations.


## Tech Stack: <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/1736c708-3547-4ef3-9a82-c89c10cd6bbf" height="80" width="80"> <br>
* AI Reference Kit Library from Intel: Leveraged for its AI capabilities, including natural language processing (NLP) for disease prediction and voice data generation.
* Streamlit: Utilized as the frontend framework to create an intuitive and user-friendly interface for the application.
* Python
* Flask: Employed as the backend framework to handle server-side logic, routing, and data processing.
* Intel Developer Cloud (IDC): Used as the cloud infrastructure, ensuring scalability and reliability.

   
## Step-by-Step Code Execution Instructions:<img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/67b8682b-3233-4301-81d1-d9617fc78404" height="80" width="80"> <br>

  This Section must contain a set of instructions required to clone and run the prototype so that it can be tested and deeply analyzed


## Drug Recommendation <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/95ac11fe-820d-4e13-92e6-77ce88a3463c" height="80" width="80"> <br>
Disease-Specific Recommendations:

 ⭐ The system provides targeted drug recommendations based on the user's reported disease, focusing on Depression, Birth Control, Diabetes Type 2, and High Blood Pressure.<br>
 ⭐ Utilizing sentiment analysis, the system assesses user reviews to gauge the overall satisfaction and effectiveness of specific drugs for the chosen disease.<br>
 ⭐ The system provides the top three drug recommendations for the selected disease, prioritizing those with the highest user ratings and usefulness counts.<br>
 ⭐ The system filters drugs with user ratings above a specified threshold (e.g., 9) to ensure that recommended drugs have a high level of user satisfaction.<br>
 ⭐ The system prioritizes the privacy and security of user data, adhering to data protection regulations and ethical standards.<br>
 ⭐ The system is designed to be accessible to a wide range of users, including those with disabilities, ensuring equitable access to healthcare information.<br>
	
<h2>
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/99f4aeca-42cd-48ad-841a-b8dacd67700c" alt="Logo">
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/1b557398-df28-46dd-ac21-8b0728d0c09f" alt="Logo">
</h2> 
<br>


<details> 
  <summary><h2>How to Run</h2><img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/23f5a395-7028-4741-9483-d4d438b00871" height="60" width="60"> <br></summary>
<h3>Introduction</h3>
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/f32172e6-85b3-410a-a229-cf3a9cfb2f89" alt="Logo" height="500">
 
  ```shell
git clone https://www.github.com/oneapi-src/disease-prediction
```
  The `setupenv.sh` can be used to automate the creation of a conda environment for execution of the algorithms using the statements below.

```shell
bash setupenv.sh
1. stock
2. intel
? 2
```

This script utilizes the dependencies found in the `env/intel/intel.yml` file to create an environment as follows:

**YAML file**                                 | **Environment Name** |  **Configuration** |
| :---: | :---: | :---: |
`env/intel/intel.yml`             | `disease_pred_intel` | Python=3.8.x, Intel® Extension for PyTorch* v1.11, Intel® Neural Compressor v1.12 |

The `run_training.py` script includes a command line flag `--intel` which enables these optimizations.    

The training process with Intel® Extension for PyTorch* can be enabled using the `run_training.py` script as:

```shell
cd src
conda activate disease_pred_intel
python run_training.py --logfile ../logs/intel.log --save_model_dir ../saved_models/intel --data_dir ../data/disease-prediction --intel
```
which will output a saved model at `saved_models/intel` and log timing information to `logs/intel.log`.
```shell
cd src
conda activate disease_pred_intel
python run_training.py --logfile ../logs/intel.log --save_model_dir ../saved_models/intel --data_dir ../data/disease-prediction --intel --bf16
```

The inference process with Intel® Extension for PyTorch* and Intel OpenMP enabled can be run using the `run_inference.py` script as follows:

```shell
cd src
conda activate disease_pred_intel
python -m intel_extension_for_pytorch.cpu.launch --disable_numactl run_inference.py --saved_model_dir ../saved_models/intel --input_file ../data/disease-prediction/Testing.csv --batch_size 20 --intel
```

which outputs a json string of the *predicted probabilities Top 5 diagnoses for each entry in the input file*, processing at batch size of 20.

Once the model is ready and can be used run 
```shell
cd data
streamlit run main.py
```

 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/99f4aeca-42cd-48ad-841a-b8dacd67700c" alt="Logo">
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/1b557398-df28-46dd-ac21-8b0728d0c09f" alt="Logo">
 <br>
  
</details>

## First Aid <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/95ac11fe-820d-4e13-92e6-77ce88a3463c" height="80" width="80"> <br>
Disease-Specific Recommendations:

 ⭐ The system provides targeted drug recommendations based on the user's reported disease, focusing on Depression, Birth Control, Diabetes Type 2, and High Blood Pressure.<br>
 ⭐ Utilizing sentiment analysis, the system assesses user reviews to gauge the overall satisfaction and effectiveness of specific drugs for the chosen disease.<br>
 ⭐ The system provides the top three drug recommendations for the selected disease, prioritizing those with the highest user ratings and usefulness counts.<br>
 ⭐ The system filters drugs with user ratings above a specified threshold (e.g., 9) to ensure that recommended drugs have a high level of user satisfaction.<br>
 ⭐ The system prioritizes the privacy and security of user data, adhering to data protection regulations and ethical standards.<br>
 ⭐ The system is designed to be accessible to a wide range of users, including those with disabilities, ensuring equitable access to healthcare information.<br>
	
<h2>
 
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/4168dae8-087d-43dd-83a9-dbcf26a1103e" alt="Logo">
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/df0a966c-2473-4aac-871d-ffb5295aaa5a" alt="Logo" height="500" width="600">
 
</h2> 
<br>



<details> 
  <summary><h2>How to Run</h2><img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/f062e7f5-8d80-4b05-8b0c-f18c87b1321d" height="60" width="60"> <br></summary>
<h3>Introduction</h3>
<img src="https://github.com/oneapi-src/voice-data-generation/blob/main/assets/E2E_stock.png" alt="Logo">

```
git clone https://github.com/oneapi-src/voice-data-generation
cd voice-data-generation
```

##### 2.2 Data preparation
> The LJSpeech audio files dataset is downloaded and extracted in a folder before running the training python module.

Folder structure Looks as below after extraction of dataset.
```
- data
    - LJSpeech-1.1
      - wavs
      - metadata
      - readme
```
> **Note**: For instructions to download the dataset, refer the **data.txt** file inside "data" folder.

> **Now the data folder contains the below structure** 
<br>data="data/LJSpeech-1.1/{wavs/metadata/readme}"

> **Note**: Please be in "WaveRNN" folder to continue benchmarking. the below step is optional, if user already followed the instructions provided above in data preperation.
```
cd WaveRNN 
```
```
Run the preprocess module as given below to start data preprocessing using the active environment.
<br>This module takes option to run the preprocessing.
```

#### 3 Training model
Run the training module as given below to start training using the active environment. 

<br>This module takes option to run the training.
```
usage: training.py [-h] [--force_gta] [--force_cpu] [--lr LR] [--batch_size BATCH_SIZE] [--hp_file FILE] [--epochs EPOCHS]

Train Tacotron TTS & WaveRNN Voc

```
**Command to run training**
```sh
python training.py --hp_file 'hparams.py' --epochs 100
```

 **Note**: Users can evaluate the models in two ways 
1. Single text sentence
2. Multiple text sentences using csv file.

```sh
# Evaluating on the single input string
python evaluation.py --input_text "From fairest creatures we desire increase, That thereby beauty's rose" -b -ipx 0 --voc_weights 'pretrained/voc_weights/latest_weights.pyt' --tts_weights 'pretrained/tts_weights/latest_weights.pyt'
```
```sh
# Evaluating on multiple text sentences using csv file
python evaluation.py --input_text "../../data/product_description.csv" -b -ipx 0 --voc_weights 'pretrained/voc_weights/latest_weights.pyt' --tts_weights 'pretrained/tts_weights/latest_weights.pyt'
```

  
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/4168dae8-087d-43dd-83a9-dbcf26a1103e" alt="Logo">
 <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/df0a966c-2473-4aac-871d-ffb5295aaa5a" alt="Logo" height="500" width="600">
 
</details>

<h3>How I did?</h3>
   
✅ Utilized 2 or more AI Reference Kits as the foundation of the submission's super kit services.<br><br>
✅ Deployed each service, including the frontend, inside a Docker container. <br><br>
✅ Leveraged the Intel AI Software Optimizations present in the selected AI Reference Kits for improved performance.<br><br>
✅ Ensured that the front-end interacted with the back-end APIs using HTTP protocols.
   


## What I Learned: <img src="https://github.com/JoelJJoseph/oneapi-sa-hack/assets/72274851/717e8fc7-98cf-4370-a425-21c948590a20" height="80" width="80"> <br>
We delve into the key learnings and technologies utilized during the creation of our project. By harnessing a diverse set of cutting-edge technologies, I aimed to develop an innovative solution that seamlessly integrates multiple domains.
* Learned how to implement modern AI application design architectures.
* Gained access to the latest hardware resources available on the Intel Developer Cloud.
* Acquired hands-on experience in building optimized end-to-end AI applications.
* Utilized 2 or more AI Reference Kits as the foundation of the submission's super kit services.
* Collaborated with Intel experts to enhance solutions using Intel technologies.
* Deployed each service, including the frontend, inside a Docker container.
* Leveraged the Intel AI Software Optimizations present in the selected AI Reference Kits for improved performance.
* Ensured that the front-end interacted with the back-end APIs using HTTP protocols.
* Implemented a data store bound to the containers for storage of models, data, and model outputs.
