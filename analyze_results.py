import { ChatGPTAPI } from 'chatgpt';
import fs from 'fs';
import dotenv from 'dotenv';

dotenv.config();

const apiKey = process.env.OPENAI_API_KEY;

if (!apiKey) {
    throw new Error('API key not found');
}

const chatAPI = new ChatGPTAPI({
    apiKey: apiKey,
    apiBaseUrl: process.env.OPENAI_API_ENDPOINT || 'https://api.openai.com/v1',
    completionParams: {
        model: process.env.MODEL || 'gpt-3.5-turbo',
        temperature: +(process.env.TEMPERATURE || 0) || 1,
        top_p: +(process.env.TOP_P || 0) || 1,
        max_tokens: process.env.MAX_TOKENS ? +process.env.MAX_TOKENS : undefined,
    },
});

const generatePrompt = (testResults) => {
    const answerLanguage = process.env.LANGUAGE
        ? `Answer me in ${process.env.LANGUAGE},`
        : '';

    const prompt = process.env.PROMPT ||
        'Below are the test results. Please analyze the failures and provide feedback along with the correct code:';

    return `${prompt} ${answerLanguage}:
    ${testResults}
    `;
};

const analyzeTestResults = async () => {
    const testResults = fs.readFileSync('build/result.log', 'utf-8');
    const prompt = generatePrompt(testResults);

    console.time('code-review cost');
    const res = await chatAPI.sendMessage(prompt);
    console.timeEnd('code-review cost');

    fs.writeFileSync('feedback.log', res.text);
};

analyzeTestResults().catch(console.error);
