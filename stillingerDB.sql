CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    location VARCHAR(255),
    description TEXT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


INSERT INTO jobs (title, location, description) VALUES
('Systemutvikler', 'Oslo', 'Vi søker en dyktig systemutvikler med erfaring innen Java og Python. Du vil jobbe med spennende prosjekter og ha muligheten til å utvikle dine ferdigheter i et dynamisk miljø.'),
('UX Designer', 'Trondheim', 'Vi søker en kreativ UX Designer med erfaring i brukertest og prototyping. Du vil arbeide med å designe brukervennlige løsninger for våre digitale produkter.'),
('Data Scientist', 'Bergen', 'Vi søker en analytisk Data Scientist med erfaring i maskinlæring og statistisk analyse. Du vil jobbe med store datamengder for å finne innsikter som kan forbedre våre tjenester.'),
('Prosjektleder', 'Oslo', 'Vi søker en erfaren prosjektleder med gode lederegenskaper og evne til å koordinere tverrfaglige team. Du vil være ansvarlig for å sikre at prosjektene våre leveres i tide og innenfor budsjett.'),
('Frontend Utvikler', 'Trondheim', 'Vi søker en dyktig frontend utvikler med erfaring i React og JavaScript. Du vil jobbe med å utvikle og forbedre brukergrensesnittet for våre webapplikasjoner.');
