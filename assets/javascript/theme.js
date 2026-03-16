export const THEME_CLASSES = {
    // Contenedor de Marca/Logo (Navbar y Footer) 
    brand: "flex items-center gap-3 text-xl font-bold tracking-tight transition-colors",
    brandText: "text-slate-900 dark:text-white", 
    logoLight: "h-10 w-auto object-contain dark:hidden", // Se oculta en modo oscuro 
    logoDark: "h-10 w-auto object-contain hidden dark:block", // Se muestra en modo oscuro 

    // Base para botones con estilo "Pill" y sombra 
    buttonBase: "px-6 py-2 rounded-full font-semibold transition-all duration-300 shadow-md active:scale-95",
    
    // Variantes de botones basadas en el color 'primary' del sitio 
    btnPrimary: "bg-blue-700 text-white hover:bg-blue-800 dark:bg-blue-600 dark:hover:bg-blue-500 shadow-blue-900/20",
    btnSecondary: "bg-slate-200 text-slate-800 hover:bg-slate-300 dark:bg-slate-800 dark:text-slate-100",
    
    // Enlaces de la Navbar
    navLink: "text-slate-600 hover:text-blue-700 dark:text-slate-300 dark:hover:text-white font-medium transition-colors",
    
    // Enlaces del Footer
    socialLink: "text-slate-500 hover:text-blue-700 dark:text-slate-400 dark:hover:text-white text-2xl transition-all duration-300 hover:scale-110 inline-block px-2",
    
    // Toggle modo oscuro/claro
    themeToggle: "p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-all duration-300 text-slate-600 dark:text-yellow-400 text-xl",
};