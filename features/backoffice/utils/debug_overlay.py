def show_debug_overlay(driver, text):
    driver.execute_script(f"""
        let div = document.getElementById('qa-debug-overlay');

        if (!div) {{
            div = document.createElement('div');
            div.id = 'qa-debug-overlay';
            div.style.position = 'fixed';
            div.style.top = '10px';
            div.style.right = '10px';
            div.style.zIndex = '999999';
            div.style.backgroundColor = 'rgba(0,0,0,0.85)';
            div.style.color = 'white';
            div.style.padding = '12px';
            div.style.borderRadius = '8px';
            div.style.fontFamily = 'Arial';
            div.style.fontSize = '13px';
            document.body.appendChild(div);
        }}

        div.innerHTML = `{text}`;
    """)