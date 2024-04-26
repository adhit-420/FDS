chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension installed');
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.greeting === 'hello') {
        console.log('Received message:', request.greeting);
        sendResponse({ farewell: 'goodbye' });
    }
});