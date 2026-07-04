/*
|--------------------------------------------------------------------------
| AI Blog Generator Authentication
|--------------------------------------------------------------------------
*/

/*----------------------------------------------------------
 CSRF Helper
----------------------------------------------------------*/

function getCSRFToken() {

    const token = document.querySelector(
        "[name=csrfmiddlewaretoken]"
    );

    return token ? token.value : "";

}

/*----------------------------------------------------------
 Create Django Session
----------------------------------------------------------*/

async function createDjangoSession(accessToken) {

    console.log("Creating Django session...");

    const response = await fetch("/create-session/", {

        method: "POST",

        headers: {

            "Content-Type": "application/json",

            "X-CSRFToken": getCSRFToken(),

        },

        credentials: "same-origin",

        body: JSON.stringify({

            access_token: accessToken,

        }),

    });

    const result = await response.json();

    console.log("Django Session Response:", result);

    return result;

}

/*----------------------------------------------------------
 Email Login
----------------------------------------------------------*/

async function login(email, password) {

    const { data, error } =
        await window.supabaseClient.auth.signInWithPassword({

            email,

            password,

        });

    if (error) {

        throw error;

    }

    await finishLogin(data.session);

}

/*----------------------------------------------------------
 Signup
----------------------------------------------------------*/

async function signup(email, password) {

    const { data, error } =
        await window.supabaseClient.auth.signUp({

            email,

            password,

        });

    if (error) {

        throw error;

    }

    return data;

}

/*----------------------------------------------------------
 Google OAuth
----------------------------------------------------------*/

async function loginWithGoogle() {

    window.location.href =
        "https://szzyrbpekghxnlxaijwd.supabase.co/auth/v1/authorize" +
        "?provider=google" +
        "&redirect_to=" +
        encodeURIComponent(window.location.origin + "/oauth/");

}
/*----------------------------------------------------------
 GitHub OAuth
----------------------------------------------------------*/

async function loginWithGithub() {

    console.log("GitHub Login Started");

    const { data, error } =
        await window.supabaseClient.auth.signInWithOAuth({

            provider: "github",

            options: {

                redirectTo:
                    window.location.origin + "/oauth/",

            },

        });

    console.log("OAuth Data:", data);
    console.log("OAuth Error:", error);

    if (error) {

        throw error;

    }

    if (data?.url) {

        window.location.assign(data.url);

    }

}

/*----------------------------------------------------------
 Logout
----------------------------------------------------------*/

async function logout() {

    await window.supabaseClient.auth.signOut();

    await fetch("/logout/", {

        method: "POST",

        headers: {

            "X-CSRFToken": getCSRFToken(),

        },

        credentials: "same-origin",

    });

    window.location.href = window.LOGIN_URL;

}

/*----------------------------------------------------------
 Forgot Password
----------------------------------------------------------*/

async function forgotPassword(email) {

    const { error } =
        await window.supabaseClient.auth.resetPasswordForEmail(
            email
        );

    if (error) {

        throw error;

    }

}

/*----------------------------------------------------------
 Helpers
----------------------------------------------------------*/

function disableButton(button, text) {

    button.disabled = true;

    button.innerHTML = text;

}

function enableButton(button, text) {

    button.disabled = false;

    button.innerHTML = text;

}

/*----------------------------------------------------------
 Finish Login
----------------------------------------------------------*/

async function finishLogin(session) {

    console.log("Finishing Login");

    if (!session) {

        throw new Error("No Supabase session found.");

    }

    const response =
        await createDjangoSession(
            session.access_token
        );

    if (!response.success) {

        throw new Error(response.message);

    }

    console.log("Login Successful");

    window.location.href = window.DASHBOARD_URL;

}

/*----------------------------------------------------------
 Export Globals
----------------------------------------------------------*/

window.login = login;

window.signup = signup;

window.logout = logout;

window.loginWithGoogle = loginWithGoogle;

window.loginWithGithub = loginWithGithub;

window.createDjangoSession = createDjangoSession;

window.disableButton = disableButton;

window.enableButton = enableButton;

window.forgotPassword = forgotPassword;