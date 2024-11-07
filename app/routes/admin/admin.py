from flask import Blueprint, render_template
from app.models.user import User

admin_bp = Blueprint('admin',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/admin/static')

@admin_bp.route('/adm')
def adm():
    return render_template('adm.html')


@admin_bp.route('/report')
# @login_required
def report():
    # if not current_user.is_admin:
    #     return redirect(url_for('main.index'))
    
    users_info = User.gen_report()

    print(users_info)

    return render_template('report.html', users_info=users_info)


@admin_bp.route('/view-logs')
# @login_required
def view_logs():
    # if not current_user.is_admin:
    #     return redirect(url_for('main.index'))
    
    return render_template('view-logs.html')