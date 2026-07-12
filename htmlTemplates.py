<<<<<<< HEAD
css = """
<style>

.stChatMessage{

    border-radius:15px;

    padding:15px;

    margin-bottom:15px;

}

.stChatInput textarea{

    font-size:16px;

}

</style>
"""
=======
css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
}

.user {
    background-color: #F3F4F6;
}

.bot {
    background-color: #E5E7EB;
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/graident-ai-robot-vectorart_78370-4114.jpg?size=338&ext=jpg&ga=GA1.1.2082370165.1715644800&semt=sph" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvTNRxAKdj1QyM_mpJdf0fUxxrvimMB-ADAQ&s" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
>>>>>>> ace05383bf6b936ffedf96bf475aac8f5203b12a
