document.addEventListener(
    "DOMContentLoaded",
    initializeLogin
);

async function initializeLogin() {

    const authenticated = await syncSupabaseSession();

    if (authenticated) {
        window.location.href = "/dashboard/";
        return;
    }

    const loginBtn = document.getElementById("loginBtn");
    const googleBtn = document.getElementById("googleBtn");
    const githubBtn = document.getElementById("githubBtn");

    if (!loginBtn || !googleBtn || !githubBtn) {
        console.error("Login page elements not found.");
        return;
    }

    loginBtn.addEventListener("click", login);
    googleBtn.addEventListener("click", signInWithGoogle);
    githubBtn.addEventListener("click", signInWithGithub);
}

async function login() {

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    const { data, error } =
        await loginWithEmail(
            email,
            password
        );

    if (error) {

        alert(error.message);
        return;

    }

    const result =
        await createBackendSession(
            data.session.access_token
        );

    if (!result.success) {

        alert(result.message);
        return;

    }

    window.location.href = "/dashboard/";

}