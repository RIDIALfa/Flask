from wtforms import Form, StringField, TextAreaField, SelectField,validators


class PostForm(Form):
    title=StringField('title',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Titre"})
    message=TextAreaField('message', [validators.DataRequired()], render_kw={"placeholder":"Message"})



class CommentForm(Form):
    title=StringField('title',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Titre"})
    message=TextAreaField('message', [validators.DataRequired()], render_kw={"placeholder":"Message"})


class ALbumForm(Form):
    title=StringField('title',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Titre"})


class TodoForm(Form):
    title = StringField('title',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Titre"})
    etat = SelectField('Etat', choices=[(1, 'En cours'), (2, 'A faire'), (3, 'Terminé')])



class PhotoForm(Form):
    title = StringField('title',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Titre"})
    url = StringField('url',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"url"})
    thumbnail = StringField('thumbnail',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"ThumbnailUrl"})



class UserForm(Form):
    fullname = StringField('fullname',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Nom complet"})
    username = StringField('username',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Nom d'utilisateur"})
    email = StringField('email',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Adresse email"})
    phone = StringField('phone',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Numéro de téléphone"})
    website = StringField('website',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Lien du site web"})
    ville = StringField('ville',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Ville"})
    rue = StringField('rue',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Rue"})
    suite = StringField('suite',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Suite"})
    zipcode = StringField('zipcode',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Code postal"})
    lat = StringField('lat',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Coordonnée latitude"})
    long = StringField('long',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Coordonnée longitude"})
    compagny = StringField('compagny',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Nom de la compagnie"})
    bs = StringField('bs',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Bs"})
    catch = StringField('catch',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"catchPhrase"})
   