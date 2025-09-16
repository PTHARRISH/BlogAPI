
const ResponsiveNavBar = () => {
    return (
        <nav className="max-container padding-x py-6 max-md:block hidden dark:text-[#FFFFFF]">
            <ul className="flex items-center  justify-center gap-6 text-[#3B3C4A] lg:flex-1 dark:text-[#FFFFFF]">
                <li>
                      Hi, Harrish P T  
                </li>
                    <li>   
                        Logout
                    </li>
                    <li>Login</li>
                    <li>
                    Register
                    </li>
                
            </ul>
        </nav>
    );
};

export default ResponsiveNavBar;