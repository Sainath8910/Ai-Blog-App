/*
|--------------------------------------------------------------------------
| AI Blog Generator
| Authentication Service
|--------------------------------------------------------------------------
*/

(function () {

    /*----------------------------------------------------------
    CSRF Token
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

        if (!response.ok) {

            throw new Error(
                result.message || "Unable to create Django session."
            );

        }

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

    if (!data.session) {

        throw new Error(
            "No active session returned from Supabase."
        );

    }

    await createDjangoSession(

        data.session.access_token

    );

    return data.user;

}
    /*----------------------------------------------------------
Email Signup
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

    return data.user;

}

    /*----------------------------------------------------------
    Google OAuth
    ----------------------------------------------------------*/

    async function loginWithGoogle() {

        const { error } =
            await window.supabaseClient.auth.signInWithOAuth({

                provider: "google",

                options: {

                    redirectTo:
                        window.location.origin + "/oauth/",

                },

            });

        if (error) {

            throw error;

        }

    }

    /*----------------------------------------------------------
    GitHub OAuth
    ----------------------------------------------------------*/

    async function loginWithGithub() {

        const { error } =
            await window.supabaseClient.auth.signInWithOAuth({

                provider: "github",

                options: {

                    redirectTo:
                        window.location.origin + "/oauth/",

                },

            });

        if (error) {

            throw error;

        }

    }

    /*----------------------------------------------------------
Logout
----------------------------------------------------------*/

async function logout() {

    try {

        await window.supabaseClient.auth.signOut();

    }

    catch (error) {

        console.error(error);

    }

    await fetch(

        "/logout/",

        {

            method: "POST",

            headers: {

                "X-CSRFToken": getCSRFToken(),

            },

            credentials: "same-origin",

        }

    );

    window.location.href =

        window.LOGIN_URL;

}

    /*----------------------------------------------------------
    Forgot Password
    ----------------------------------------------------------*/

    async function forgotPassword(email) {

        const { error } =
            await window.supabaseClient.auth.resetPasswordForEmail(

                email,

                {

                    redirectTo:
                        window.location.origin + "/reset-password/",

                }

            );

        if (error) {

            throw error;

        }

    }
    async function updatePassword(password) {

    const { error } =
        await window.supabaseClient.auth.updateUser({

            password,

        });

    if (error) {

        throw error;

    }

}
    /*----------------------------------------------------------
    Expose Public API
    ----------------------------------------------------------*/

    window.Auth = {

        login,

        signup,

        logout,

        loginWithGoogle,

        loginWithGithub,

        forgotPassword,

        createDjangoSession,
        updatePassword,

    };

})();