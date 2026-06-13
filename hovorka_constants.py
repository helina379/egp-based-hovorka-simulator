class HovorkaConstants:
    def __init__(self, BW=70.0, u_basal=12.9127):
        # Patient parameters
        self.BW = BW                        # Body weight (kg)

        # Glucose subsystem
        self.F01 = 0.00097 * BW             # Non-insulin dependent glucose flux
        self.Vg = 0.16 * BW                 # Distribution volume of glucose (L)
        self.k12 = 0.066                    # Transfer rate Q2->Q1 (min^-1)
        self.Mwg = 180.0                    # Molecular weight of glucose (g/mol)
        self.Gb = 90.0                      # Basal Glucose (mg/dL)
        self.Gth = 60.0                     # Renal threshold (mg/dL)
        
        # Updated/New rates from EGP6 code
        self.kp2 = 0.0007                   # Liver glucose effectiveness 
        self.ke1 = 0.007                    # Glucometric filtration rate
        
        # Insulin subsystem
        self.Vi = 0.12 * BW                 # Distribution volume of insulin (L)
        self.tau_s = 55.0                   # Time constant for SC insulin absorption (min)
        self.ke = 0.02                      # Insulin elimination rate (min^-1)
        self.k21 = 0.045                    # Inter-compartmental insulin transfer rate
        self.kd = 0.0021                    
        self.ka = 0.02                      

        # Meal absorption
        self.Ag = 0.8                       # CHO bioavailability
        self.tau_d = 40.0                   # Time constant for meal absorption (min)

        # Insulin action
        self.ka1 = 0.006                    # Deactivation rate x1 (min^-1)
        self.ka2 = 0.06                     # Deactivation rate x2 (min^-1)
        self.ka3 = 0.03                     # Deactivation rate x3 (min^-1)
        self.Sit = 51.2e-4                  
        self.Sid = 8.2e-4                   
        self.Sie = 520e-4                   
        self.kb1 = self.Sit * self.ka1
        self.kb2 = self.Sid * self.ka2
        self.kb3 = self.Sie * self.ka3

        # EGP6 Hepatic Subsystem Parameters
        self.K6gp = 0.034
        self.Sc = 297.0
        self.cth = 8.0e-6
        self.tD = 59.9
        self.z = 23.24
        self.Ggng1b = 0.495
        self.Ggg1b = 0.7425
        self.n = 0.01
        self.rho = 0.86
        self.sigma = 0.01e-7
        self.S = 0.98e-7
        self.cb = 58.0e-7

        # Basal insulin input
        self.u_basal = u_basal            

        # Initial conditions (Matching State Space Initialization)
        self.u0 = u_basal
        self.S1_0 = u_basal * self.tau_s
        self.S2_0 = u_basal * self.tau_s
        self.I_0 = u_basal / (0.01656 * BW)
        self.x1_0 = 0.30898 * u_basal / BW
        self.x2_0 = 0.04951 * u_basal / BW
        self.x3_0 = 3.2206 * u_basal / BW
        self.G_0 = 90.0                     # Initial Plasma Glucose G (mg/dL)
        self.Gt_0 = 90.0                    # Initial Tissue Glucose Gt (mg/dL)
        self.Dm1_0 = 0.0
        self.Dm2_0 = 0.0
        self.G6p_0 = 41.897                 # Initial Glucose-6-Phosphate state
        self.c_0 = 58.0e-7                  # Initial concentration pathway state

        # Simulation Configuration
        self.MAX_TIME = 1440              
        self.h = 0.1                        # Computation step size (0.1 min)