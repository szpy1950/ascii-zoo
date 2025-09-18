from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api/chat')
def api_chat():
    message = request.args.get('msg', 'Hello there!')
    cow_type = request.args.get('cow', 'cow')
    
    try:
        # Call cow service with cow type
        response = requests.get(f'http://cow-service:8001/cow?msg={message}&type={cow_type}')
        return response.text
    except:
        return "🚫 Connection lost to the animal kingdom..."

@app.route('/')
def chat():
    message = request.args.get('msg', 'Hello there!')
    cow_type = request.args.get('cow', 'cow')
    
    try:
        # Call cow service with cow type
        response = requests.get(f'http://cow-service:8001/cow?msg={message}&type={cow_type}')
        cow_response = response.text
    except:
        cow_response = "🚫 Connection lost to the animal kingdom..."
    
    # Escape HTML in the response to prevent issues
    cow_response = cow_response.replace('<', '&lt;').replace('>', '&gt;')
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🌟 Chatty Animals - Interactive ASCII Zoo</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                overflow-x: hidden;
            }}
            
            .background-animation {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }}
            
            .floating-shapes {{
                position: absolute;
                width: 100px;
                height: 100px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                animation: float 6s ease-in-out infinite;
            }}
            
            .floating-shapes:nth-child(1) {{ top: 10%; left: 10%; animation-delay: 0s; }}
            .floating-shapes:nth-child(2) {{ top: 20%; right: 10%; animation-delay: 2s; }}
            .floating-shapes:nth-child(3) {{ bottom: 10%; left: 20%; animation-delay: 4s; }}
            .floating-shapes:nth-child(4) {{ bottom: 20%; right: 20%; animation-delay: 1s; }}
            
            @keyframes float {{
                0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
                50% {{ transform: translateY(-20px) rotate(180deg); }}
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                position: relative;
                z-index: 1;
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 40px;
                animation: slideInDown 1s ease-out;
            }}
            
            .header h1 {{
                font-size: clamp(2rem, 5vw, 4rem);
                font-weight: 700;
                background: linear-gradient(45deg, #fff, #f0f0f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 4px 20px rgba(0,0,0,0.3);
                margin-bottom: 10px;
            }}
            
            .header p {{
                color: rgba(255, 255, 255, 0.9);
                font-size: 1.2rem;
                font-weight: 300;
            }}
            
            .main-content {{
                display: grid;
                grid-template-columns: 1fr 400px;
                gap: 30px;
                animation: slideInUp 1s ease-out 0.3s both;
            }}
            
            .chat-display {{
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }}
            
            .chat-display:hover {{
                transform: translateY(-5px);
                box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            }}
            
            .chat-display::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 4px;
                background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
                background-size: 200% 100%;
                animation: shimmer 2s infinite;
            }}
            
            @keyframes shimmer {{
                0% {{ background-position: -200% 0; }}
                100% {{ background-position: 200% 0; }}
            }}
            
            .ascii-output {{
                font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
                font-size: 14px;
                line-height: 1.2;
                color: #333;
                background: #f8f9fa;
                padding: 25px;
                border-radius: 15px;
                margin: 20px 0;
                white-space: pre-wrap;
                word-wrap: break-word;
                border: 2px solid #e9ecef;
                transition: all 0.3s ease;
                animation: fadeIn 0.8s ease-out;
                position: relative;
                overflow-x: auto;
            }}
            
            .ascii-output:hover {{
                border-color: #667eea;
                background: #f0f4f8;
            }}
            
            .controls {{
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                height: fit-content;
                position: sticky;
                top: 20px;
            }}
            
            .form-group {{
                margin-bottom: 25px;
            }}
            
            .form-group label {{
                display: block;
                margin-bottom: 8px;
                font-weight: 600;
                color: #333;
                font-size: 1rem;
            }}
            
            .text-input {{
                width: 100%;
                padding: 15px 20px;
                border: 2px solid #e9ecef;
                border-radius: 12px;
                font-size: 16px;
                transition: all 0.3s ease;
                background: rgba(255, 255, 255, 0.9);
                font-family: inherit;
            }}
            
            .text-input:focus {{
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
                transform: translateY(-2px);
            }}
            
            .select-input {{
                width: 100%;
                padding: 15px 20px;
                border: 2px solid #e9ecef;
                border-radius: 12px;
                font-size: 16px;
                background: rgba(255, 255, 255, 0.9);
                cursor: pointer;
                transition: all 0.3s ease;
                appearance: none;
                background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
                background-position: right 12px center;
                background-repeat: no-repeat;
                background-size: 16px;
                padding-right: 50px;
            }}
            
            .select-input:focus {{
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
                transform: translateY(-2px);
            }}
            
            .submit-btn {{
                width: 100%;
                padding: 18px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 18px;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            
            .submit-btn:hover {{
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
            }}
            
            .submit-btn:active {{
                transform: translateY(-1px);
            }}
            
            .submit-btn::before {{
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
                transition: left 0.5s;
            }}
            
            .submit-btn:hover::before {{
                left: 100%;
            }}
            
            .animal-preview {{
                text-align: center;
                margin: 20px 0;
                font-size: 2rem;
                animation: bounce 2s infinite;
            }}
            
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                40% {{ transform: translateY(-10px); }}
                60% {{ transform: translateY(-5px); }}
            }}
            
            .status-indicator {{
                display: inline-block;
                width: 12px;
                height: 12px;
                background: #10b981;
                border-radius: 50%;
                animation: pulse 2s infinite;
                margin-right: 8px;
            }}
            
            @keyframes pulse {{
                0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
                70% {{ box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }}
                100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
            }}
            
            @keyframes slideInDown {{
                from {{ transform: translateY(-50px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            
            @keyframes slideInUp {{
                from {{ transform: translateY(50px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            
            @media (max-width: 768px) {{
                .main-content {{
                    grid-template-columns: 1fr;
                    gap: 20px;
                }}
                
                .container {{
                    padding: 15px;
                }}
                
                .chat-display, .controls {{
                    padding: 20px;
                }}
            }}
            
            .loading {{
                display: none;
                text-align: center;
                color: #667eea;
                font-weight: 600;
            }}
            
            .spinner {{
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid #f3f3f3;
                border-top: 3px solid #667eea;
                border-radius: 50%;
                animation: spin 1s linear infinite;
                margin-right: 10px;
            }}
            
            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
        </style>
    </head>
    <body>
        <div class="background-animation">
            <div class="floating-shapes"></div>
            <div class="floating-shapes"></div>
            <div class="floating-shapes"></div>
            <div class="floating-shapes"></div>
        </div>
        
        <div class="container">
            <div class="header">
                <h1>🌟 Interactive ASCII Zoo</h1>
                <p><span class="status-indicator"></span>Connect with amazing creatures through code</p>
            </div>
            
            <div class="main-content">
                <div class="chat-display">
                    <h3>💬 Conversation</h3>
                    <div class="ascii-output">{cow_response}</div>
                    <div class="loading">
                        <div class="spinner"></div>
                        Summoning your chosen creature...
                    </div>
                </div>
                
                <div class="controls">
                    <form id="chatForm" onsubmit="return sendMessage(event)">
                        <div class="form-group">
                            <label for="message">✨ Your Message</label>
                            <input 
                                type="text" 
                                id="message"
                                name="msg" 
                                value="{message}" 
                                placeholder="Type your message to the animals..." 
                                class="text-input"
                                required
                            />
                        </div>
                        
                        <div class="form-group">
                            <label for="animal">🦄 Choose Your Creature</label>
                            <select name="cow" id="animal" class="select-input" onchange="updatePreview()">
                                <option value="cow" {'selected' if cow_type == 'cow' else ''}>🐄 Classic Cow</option>
                                <option value="sheep" {'selected' if cow_type == 'sheep' else ''}>🐑 Fluffy Sheep</option>
                                <option value="dragon" {'selected' if cow_type == 'dragon' else ''}>🐲 Mighty Dragon</option>
                                <option value="elephant" {'selected' if cow_type == 'elephant' else ''}>🐘 Wise Elephant</option>
                                <option value="tux" {'selected' if cow_type == 'tux' else ''}>🐧 Tux Penguin</option>
                            </select>
                        </div>
                        
                        <div class="animal-preview" id="preview">
                            {'🐄' if cow_type == 'cow' else '🐑' if cow_type == 'sheep' else '🐲' if cow_type == 'dragon' else '🐘' if cow_type == 'elephant' else '🐧'}
                        </div>
                        
                        <button type="submit" class="submit-btn">
                            🚀 Start Conversation
                        </button>
                    </form>
                </div>
            </div>
        </div>
        
        <script>
            function updatePreview() {{
                const select = document.getElementById('animal');
                const preview = document.getElementById('preview');
                const emojis = {{
                    'cow': '🐄',
                    'sheep': '🐑', 
                    'dragon': '🐲',
                    'elephant': '🐘',
                    'tux': '🐧'
                }};
                preview.textContent = emojis[select.value] || '🐄';
            }}
            
            function showLoading() {{
                const loading = document.querySelector('.loading');
                const output = document.querySelector('.ascii-output');
                loading.style.display = 'block';
                output.style.opacity = '0.5';
            }}
            
            function hideLoading() {{
                const loading = document.querySelector('.loading');
                const output = document.querySelector('.ascii-output');
                loading.style.display = 'none';
                output.style.opacity = '1';
            }}
            
            async function sendMessage(event) {{
                event.preventDefault(); // Prevent form submission and page refresh
                
                const message = document.getElementById('message').value;
                const animal = document.getElementById('animal').value;
                
                if (!message.trim()) {{
                    return false;
                }}
                
                showLoading();
                
                try {{
                    // Make AJAX request to get cow response
                    const response = await fetch(`/api/chat?msg=${{encodeURIComponent(message)}}&cow=${{animal}}`);
                    const data = await response.text();
                    
                    // Update the ASCII output without refreshing
                    const output = document.querySelector('.ascii-output');
                    output.textContent = data;
                    
                    // Add fade-in animation
                    output.style.animation = 'none';
                    output.offsetHeight; // Trigger reflow
                    output.style.animation = 'fadeIn 0.8s ease-out';
                    
                    // Clear the message input for next conversation
                    document.getElementById('message').value = '';
                    document.getElementById('message').focus();
                    
                }} catch (error) {{
                    console.error('Error:', error);
                    const output = document.querySelector('.ascii-output');
                    output.textContent = '🚫 Connection lost to the animal kingdom...';
                }} finally {{
                    hideLoading();
                }}
                
                return false;
            }}
            
            // Auto-focus message input
            document.getElementById('message').focus();
            
            // Add keyboard shortcuts
            document.addEventListener('keydown', function(e) {{
                if (e.ctrlKey && e.key === 'Enter') {{
                    sendMessage(e);
                }}
            }});
            
            // Initialize preview
            updatePreview();
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

