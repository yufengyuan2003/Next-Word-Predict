# Next-Word-Predict
# Project Introduction  
  
1. **Background**  
  
On smartphones, the prediction function of the keyboard has become a ubiquitous feature in users' daily lives, greatly enhancing input efficiency. However, why this feature is less commonly applied on computers is a question we aim to address in this project. Through in-depth research and practice, we hope to not only explore the possibility of implementing input prediction in a computer environment, but also understand the differences in the application of this technology across different platforms.  
  
2. **Motivation**  
  
Our choice of this topic is motivated not only by curiosity, but also by a desire to improve human-computer interaction and pursue technological innovation. By analyzing mobile keyboard inputs, we hope to unlock their underlying mechanisms and apply them to computer environments. Additionally, we are aware that models like GPT-2 can predict the next word to a certain degree. However, GPT-2 can only predict the single most appropriate word, which does not align with users' practical needs. In fact, to enhance the keyboard on a computer, we require not only the most precise word, but multiple prediction options to facilitate users' ability to choose the desired word. Furthermore, this reflects a critical examination of current computer input methods, exploring the possibility of enhancing user experience through the integration of prediction features.  
  
3. **Project Objectives**  
  
Our project aims to develop a system that can accurately predict user input on a computer. By comparing the differences between mobile and computer inputs, we aim to understand why prediction is more challenging on some platforms. Additionally, our system will incorporate memory functionality for user inputs, aligning with individual preferences. By achieving these objectives, we hope to not only improve computer input efficiency, but also provide valuable insights for future innovations in human-computer interaction.  
  
# Relevant Preparations  
  
After selecting input prediction as our project focus, we conducted a literature review to gain a better understanding of current research status and advancements in this field.  
  
1. **Analysis of Input Prediction Principles**  
  
Numerous studies have delved into the principles of input prediction, particularly in the context of successful mobile keyboard implementations. These studies encompass statistical models based on user history inputs and neural network models utilizing deep learning techniques. By deeply exploring these principles, we aim to comprehend why mobile keyboard inputs excel at predicting users' next words.  
  
2. **Research in the Natural Language Processing Domain**  
  
The field of natural language processing (NLP) has examined various aspects of text generation and language models. Some works have explored context-based word prediction, which can serve as a source of inspiration for our project. For instance, large language models like ChatGPT consider context when generating text, an idea that can be borrowed for predicting the next word.  
  
3. **Improvements to Traditional Keyboard Input Methods**  
  
Research has also focused on refining traditional keyboard input methods. Techniques such as layout optimization and keystroke probability models aim to enhance user input efficiency. While these efforts primarily target traditional keyboard inputs, they offer insights into enhancing input efficiency that can be applied to our project.  
  
Through a thorough examination of these related works, we can extract valuable lessons learned and identify suitable methods and technologies for our project. This provides a solid theoretical foundation and practical guidance for our efforts.  
  
# Dataset Selection  
  
Given our objective of creating an input prediction system for daily use, we paid attention to selecting datasets with language that closely aligns with real-life scenarios. Ultimately, after screening various sources, we excluded online collections of Chinese and English casual language and added two books: "The Kite Runner" and "Ordinary People" in Chinese, and "Game of Thrones" in English. These additions aim to enrich our dataset with more authentic language materials suitable for daily communication contexts.
# 项目介绍  
  
1. **问题背景**  
  
在智能手机上，输入法的预测功能已经成为用户日常生活中的一部分，极大地提高了输入效率。然而，为何在电脑上这一功能相对较少被应用，是我们在项目中尝试解决的问题。通过深入研究和实践，我们希望不仅能够探索在电脑环境中实现输入预测的可能性，还能了解这一技术在不同平台上的应用差异。  
  
2. **选择动机**  
  
我们选择这一课题的动机并非仅仅是出于好奇心，更是基于对人机交互的改善和技术创新的追求。通过分析手机输入法，我们希望挖掘其中的潜在机制，并将其应用于电脑环境中。同时，我们也了解到GPT-2可以一定程度上实现对于下一个单词预测这一功能。然而，gpt2仅能预测一个最合适的单词，这不符合用户的实际用途。事实上，若要在电脑上进行输入法的完善，我们不仅需要最精确的单词，更需要多个预测结果，以方便用户自主地选择想输入的单词。此外，这也是对当前电脑输入方式的一种反思，探究是否有可能通过引入预测功能来提高用户体验。  
  
3. **项目目标**  
  
我们的项目旨在开发一个能够在电脑上准确预测用户输入的系统，并通过比较手机和电脑输入方式的不同，探索为何输入预测在这两个平台上存在差异。此外，对于输入结果的记忆功能也是我们的目标，这将使我们的输入法符合用户的个性需求。通过实现这些目标，我们希望不仅能够提高电脑输入的效率，还能够为未来改进人机交互方式提供一些有价值的思考。  
  
# 相关准备工作  
  
在选择输入预测作为项目主题之后，我们了解了相关领域的先前工作，以更好地了解当前研究的现状和前沿。  
  
1. **分析输入预测原理**  
  
许多研究致力于深入分析输入预测的原理，特别是在手机输入法的成功案例中。这些工作涵盖了基于用户历史输入的统计模型、基于深度学习的神经网络模型等方面。通过深入挖掘这些原理，我们能够更好地理解为何手机输入法在准确预测用户下一个单词方面取得了成功。  
  
2. **自然语言处理领域的研究**  
  
在自然语言处理领域，有很多研究关注文本生成和语言模型。其中，一些工作探讨了基于上下文的词汇预测，这对于我们的项目有一定的启示。例如，ChatGPT等大型语言模型在生成文本时能够考虑上下文，这种思想可以被借鉴用于预测下一个单词。  
  
3. **键盘输入方式的改进**  
  
一些研究致力于改进传统的键盘输入方式,包括使用布局优化、按键概率模型等方法，以提高用户的输入效率。虽然这些工作主要集中在改进传统的键盘输入，但它们提供了一些关于提高输入效率的启示，也能够为我们所用。  
  
通过对这些相关工作的深入研究，我们能够从已有的知识中吸取经验教训，同时找到适合我们项目的方法和技术。这为我们的项目提供了坚实的理论基础和实践参考。  
  
# 数据集选取  
  
由于我们的目的是创造一个适用于日常生活的预测输入系统，因此我们在选择数据集时也会注意挑选语言更加贴合生活的文本。最终经过筛选，除去我们在网上搜集到的中英文日常用语，我们还向中文数据集中添加了《追风筝的人》和《平凡的世界》这两本书，向英文数据集中添加了《权力的游戏》。
