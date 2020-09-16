const inboxButton = document.getElementById("inbox-dropdown-btn");
const inboxDropDown = document.getElementById('InboxDropdown');
const inboxWrapper = document.querySelector('.inbox-wrapper');
inboxButton.addEventListener('click', toggleInbox);

function toggleInbox(event) {
	event.preventDefault();
	if (inboxWrapper.style.opacity === '1') {
		inboxWrapper.style.opacity = '0';
	} else {
		inboxWrapper.style.opacity = '1';
	}
}
function showInbox(event) {
	event.preventDefault();
	inboxWrapper.style.opacity = '1';
}
// close the inbox
document.querySelector('.main-body').addEventListener('click', (event) => {
	if (!event.target.classList.contains('send-message-btn')) {
		inboxWrapper.style.opacity = '0';
	}
})


// code for chat box

const chats = document.querySelector('.chats');
const chatBox = document.getElementById('InboxDropdownChat');
const backButton = document.getElementById('chatbox-back-btn');

// these global vars are changes everytime user click on the other chat

let CHAT_URL;
let SENDER, RECEIVER;
function showChatBox(requestUserId, chatUserId,flag=false) {
	SENDER = requestUserId;
	RECEIVER = chatUserId;

	// UI 
	event.preventDefault();
	showInbox(event);
	if (event.target.classList.contains('chat-profile')) {
		chatBox.style.display = 'block';
	} else if (event.target.parentElement.classList.contains('chat-profile')) {
		chatBox.style.display = 'block';	
	}
	if (flag) {
		chatBox.style.display = 'block';
	}
	const messagesOutputElement = document.querySelector('.chat-messages');
	messagesOutputElement.innerHTML = '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>';
	// Getting the data from api
	const url = `/api/messages/${Number(requestUserId)}/${Number(chatUserId)}`;
	CHAT_URL = url;
	fetch(url)
		.then(response => {
			return response.json();
		}).then((data) => {
			showMessages(data);
		}).catch(error => {
			console.log(error);
		});

	

}
function showMessages({ messages }) {
	let output = '';
	const messagesOutputElement = document.querySelector('.chat-messages');
	messages.forEach(message => {
		output += `

		<div class='card chat-message'>
			<b>${message.sender} </b>
			<p>${message.message}</p>
		</div>
		`;
	});
	messagesOutputElement.innerHTML = output;
}

// Sending messages
const sendMessageButton = document.getElementById('send-msg-btn');

sendMessageButton.addEventListener('click', () => {
	const message = document.getElementById('post-message').value;
	if (message !== '') {
		sendMessageButton.innerHTML = 'Sending...';
		const data = {
			sender: SENDER,
			receiver: RECEIVER,
			message:message
		}
		fetch(CHAT_URL, {
			method: 'POST',
			headers: { 'Content-type': 'application/json' },
			body: JSON.stringify(data)
		}).then((response) => {
			return response.json();
		}).then(data => {
			// add message to the list
			const messagesOutputElement = document.querySelector('.chat-messages');
			messagesOutputElement.innerHTML += `
			<div class='card chat-message'>
			<b>${data.sender} </b>
			<p>${data.message}</p>
			</div>
			`;
			document.getElementById('post-message').value = '';
			sendMessageButton.innerHTML = 'Send';
			
		}).catch(err => {
			console.log(err);
		});
	}
});

